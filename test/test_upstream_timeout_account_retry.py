from __future__ import annotations

import queue
import sys
import tempfile
import time
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from curl_cffi import requests

from services.image_task_service import ImageTaskService, TASK_STATUS_SUCCESS
from services.openai_backend_api import OpenAIBackendAPI
from services.protocol import conversation as conversation_module
from services.protocol import openai_search, openai_v1_response as response_module, web_search_tool
from utils.helper import FirstOutputDeadline, FirstOutputTimeout, iter_sse_payloads


class QueueResponse:
    def __init__(self, *chunks: bytes | None) -> None:
        self.queue: queue.Queue[bytes | None] = queue.Queue()
        for chunk in chunks:
            self.queue.put(chunk)
        self.closed = False

    def iter_content(self):
        while True:
            chunk = self.queue.get()
            if chunk is None:
                return
            yield chunk

    def close(self) -> None:
        self.closed = True
        self.queue.put(None)


class CompletedStreamResponse:
    def __init__(self, *chunks: bytes) -> None:
        self.chunks = chunks
        self.closed = False

    def iter_content(self):
        yield from self.chunks

    def close(self) -> None:
        self.closed = True

class FailingCloseResponse(QueueResponse):
    def close(self) -> None:
        super().close()
        raise RuntimeError("stream cleanup failed")

class FakeBackend:
    def __init__(self, access_token: str = "", deadline: FirstOutputDeadline | None = None) -> None:
        self.access_token = access_token
        self.deadline = deadline
        self.closed = False

    def complete_first_output(self) -> None:
        if self.access_token == "A":
            raise FirstOutputTimeout("late first output")
        self.deadline = None

    def close(self) -> None:
        self.closed = True

class CompletedBackend(FakeBackend):
    def complete_first_output(self) -> None:
        self.deadline = None


class UpstreamTimeoutRetryTests(unittest.TestCase):
    def test_timed_sse_closes_response_on_deadline(self) -> None:
        response = QueueResponse()
        with self.assertRaises(FirstOutputTimeout):
            list(iter_sse_payloads(response, FirstOutputDeadline(0)))
        self.assertTrue(response.closed)

    def test_timed_sse_preserves_timeout_when_close_fails(self) -> None:
        with self.assertRaises(FirstOutputTimeout):
            list(iter_sse_payloads(FailingCloseResponse(), FirstOutputDeadline(0)))

    def test_normal_sse_parser_stays_unchanged_without_deadline(self) -> None:
        response = mock.Mock()
        response.iter_lines.return_value = [b"data: first", b"", b"data: [DONE]"]
        self.assertEqual(list(iter_sse_payloads(response)), ["first", "[DONE]"])

    def test_timed_sse_accepts_iter_content_end_of_stream(self) -> None:
        response = CompletedStreamResponse(b"data: complete\n")
        self.assertEqual(
            list(iter_sse_payloads(response, FirstOutputDeadline(1))),
            ["complete"],
        )

    def test_response_stream_fallback_keeps_one_setup_sequence(self) -> None:
        selected: list[set[str]] = []

        def select(excluded: set[str] | None = None) -> str:
            selected.append(set(excluded or ()))
            return "B"

        def events(backend: FakeBackend, **_kwargs: object):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no delta")
            yield {"type": "conversation.delta", "delta": "answer"}

        body = {"model": "gpt-5", "input": "hello", "stream": True}
        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", FakeBackend),
            mock.patch.object(conversation_module, "conversation_events", events),
            mock.patch.object(conversation_module.account_service, "get_text_access_token", select),
        ):
            output = list(response_module.stream_text_response(
                FakeBackend("A"), body, [{"role": "user", "content": "hello"}]
            ))

        self.assertEqual([event["type"] for event in output].count("response.created"), 1)
        self.assertEqual([event["type"] for event in output].count("response.output_item.added"), 1)
        self.assertEqual([event["type"] for event in output].count("response.output_text.delta"), 1)
        self.assertEqual(output[-1]["response"]["output"][0]["content"][0]["text"], "answer")
        self.assertEqual(selected, [{"A"}])

    def test_image_progress_output_followed_by_timeout_does_not_retry(self) -> None:
        selected: list[set[str]] = []

        class StartedBackend(FakeBackend):
            def complete_first_output(self) -> None:
                self.deadline = None

        def select(**kwargs: object) -> str:
            selected.append(set(kwargs.get("excluded_tokens") or ()))
            return "B"

        def image_stream(backend: CompletedBackend, request: conversation_module.ConversationRequest, index: int, total: int):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no image output")
            yield conversation_module.ImageOutput(kind="progress", model=request.model, index=index, total=total, text="working")
            raise FirstOutputTimeout("late")

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", CompletedBackend),
            mock.patch.object(conversation_module, "stream_image_outputs", image_stream),
            mock.patch.object(conversation_module.account_service, "get_available_access_token", select),
            mock.patch.object(conversation_module.account_service, "get_account", lambda _token: {"email": "a@example.com"}),
            mock.patch.object(conversation_module.account_service, "mark_image_result"),
        ):
            with self.assertRaises(FirstOutputTimeout):
                conversation_module._generate_single_image(
                    conversation_module.ConversationRequest(model="gpt-image-2", prompt="draw"), 1, 1
                )

        self.assertEqual(selected, [set()])

    def test_codex_image_retries_before_first_output(self) -> None:
        selected: list[set[str]] = []

        def select(**kwargs: object) -> str:
            excluded = set(kwargs.get("excluded_tokens") or ())
            selected.append(excluded)
            return "A" if len(selected) == 1 else "B"

        def codex_stream(backend: CompletedBackend, request: conversation_module.ConversationRequest, index: int, total: int):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no codex output")
            yield conversation_module.ImageOutput(kind="result", model=request.model, index=index, total=total, data=[{"b64_json": "x"}])

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", CompletedBackend),
            mock.patch.object(conversation_module, "stream_codex_image_outputs", codex_stream),
            mock.patch.object(conversation_module.account_service, "get_available_access_token", select),
            mock.patch.object(conversation_module.account_service, "get_account", lambda token: {"email": token}),
            mock.patch.object(conversation_module.account_service, "mark_image_result"),
        ):
            result = conversation_module._generate_single_image(
                conversation_module.ConversationRequest(model="pro-codex-gpt-image-2", prompt="draw"), 1, 1
            )

        self.assertEqual(len(result), 1)
        self.assertEqual(selected, [set(), {"A"}])

    def test_image_task_waits_for_inherited_account_failover(self) -> None:
        selected: list[set[str]] = []

        def select(**kwargs: object) -> str:
            excluded = set(kwargs.get("excluded_tokens") or ())
            selected.append(excluded)
            return "A" if len(selected) == 1 else "B"

        def image_stream(backend: CompletedBackend, request: conversation_module.ConversationRequest, index: int, total: int):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no image output")
            yield conversation_module.ImageOutput(kind="result", model=request.model, index=index, total=total, data=[{"b64_json": "x"}])

        def handler(payload: dict[str, object]) -> dict[str, object]:
            outputs = conversation_module._generate_single_image(
                conversation_module.ConversationRequest(model=str(payload["model"]), prompt=str(payload["prompt"])), 1, 1
            )
            return {"data": outputs[0].data, "_account_email": outputs[0].account_email}

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", CompletedBackend),
            mock.patch.object(conversation_module, "stream_image_outputs", image_stream),
            mock.patch.object(conversation_module.account_service, "get_available_access_token", select),
            mock.patch.object(conversation_module.account_service, "get_account", lambda token: {"email": token}),
            mock.patch.object(conversation_module.account_service, "mark_image_result"),
            mock.patch("services.image_task_service.log_service"),
            tempfile.TemporaryDirectory() as directory,
        ):
            service = ImageTaskService(Path(directory) / "tasks.json", generation_handler=handler)
            service.submit_generation({"id": "owner"}, client_task_id="task-1", prompt="draw", model="gpt-image-2", size="1024x1024")
            for _ in range(50):
                task = service.list_tasks({"id": "owner"}, ["task-1"])["items"][0]
                if task["status"] == TASK_STATUS_SUCCESS:
                    break
                time.sleep(0.01)

        self.assertEqual(task["status"], TASK_STATUS_SUCCESS)
        self.assertEqual(selected, [set(), {"A"}])

    def test_text_retries_timeout_account_before_delta(self) -> None:
        selected: list[set[str]] = []
        used: list[str] = []
        original_backend = FakeBackend

        def select(excluded: set[str] | None = None) -> str:
            selected.append(set(excluded or ()))
            return "B"

        def events(backend: FakeBackend, **_kwargs: object):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no delta")
            yield {"type": "conversation.delta", "delta": "ok"}

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", original_backend),
            mock.patch.object(conversation_module, "conversation_events", events),
            mock.patch.object(conversation_module.account_service, "get_text_access_token", select),
            mock.patch.object(conversation_module.account_service, "mark_text_used", used.append),
        ):
            result = list(conversation_module.stream_text_deltas(
                original_backend("A"), conversation_module.ConversationRequest(prompt="hello")
            ))

        self.assertEqual(result, ["ok"])
        self.assertEqual(selected, [{"A"}])
        self.assertEqual(used, ["B"])

    def test_text_does_not_retry_after_delta(self) -> None:
        selected: list[set[str]] = []

        class StartedBackend(FakeBackend):
            def complete_first_output(self) -> None:
                self.deadline = None
        def select(excluded: set[str] | None = None) -> str:
            selected.append(set(excluded or ()))
            return "B"

        def events(_backend: FakeBackend, **_kwargs: object):
            yield {"type": "conversation.delta", "delta": "started"}
            raise FirstOutputTimeout("late")

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", StartedBackend),
            mock.patch.object(conversation_module, "conversation_events", events),
            mock.patch.object(conversation_module.account_service, "get_text_access_token", select),
        ):
            with self.assertRaises(FirstOutputTimeout):
                list(conversation_module.stream_text_deltas(
                    StartedBackend("A"), conversation_module.ConversationRequest(prompt="hello")
                ))

        self.assertEqual(selected, [])

    def test_image_retries_timeout_account_and_excludes_it(self) -> None:
        selected: list[set[str]] = []
        marked: list[tuple[str, bool]] = []

        def select(**kwargs: object) -> str:
            excluded = set(kwargs.get("excluded_tokens") or ())
            selected.append(excluded)
            return "A" if len(selected) == 1 else "B"

        def image_stream(backend: CompletedBackend, request: conversation_module.ConversationRequest, index: int, total: int):
            if backend.access_token == "A":
                raise FirstOutputTimeout("no image output")
            yield conversation_module.ImageOutput(
                kind="result", model=request.model, index=index, total=total, data=[{"b64_json": "x"}]
            )

        with (
            mock.patch.object(conversation_module, "OpenAIBackendAPI", CompletedBackend),
            mock.patch.object(conversation_module, "stream_image_outputs", image_stream),
            mock.patch.object(conversation_module.account_service, "get_available_access_token", select),
            mock.patch.object(conversation_module.account_service, "get_account", lambda token: {"email": token}),
            mock.patch.object(conversation_module.account_service, "mark_image_result", lambda token, ok: marked.append((token, ok))),
        ):
            result = conversation_module._generate_single_image(
                conversation_module.ConversationRequest(model="gpt-image-1", prompt="draw"), 1, 1
            )

        self.assertEqual(len(result), 1)
        self.assertEqual(selected, [set(), {"A"}])
        self.assertEqual(marked, [("A", False), ("B", True)])

    def test_search_retry_is_shared_by_explicit_and_embedded_handlers(self) -> None:
        selected: list[set[str]] = []
        marked: list[str] = []

        class SearchBackend:
            def __init__(self, token: str, deadline: FirstOutputDeadline | None = None) -> None:
                self.token = token

            def search(self, prompt: str) -> dict[str, object]:
                if self.token == "A":
                    raise FirstOutputTimeout("no result")
                return {"answer": prompt, "sources": []}

            def close(self) -> None:
                pass

        def select(excluded: set[str] | None = None) -> str:
            selected.append(set(excluded or ()))
            return "A" if len(selected) in {1, 3} else "B"

        with (
            mock.patch.object(web_search_tool, "OpenAIBackendAPI", SearchBackend),
            mock.patch.object(web_search_tool.account_service, "get_text_access_token", select),
            mock.patch.object(web_search_tool.account_service, "mark_text_used", marked.append),
            mock.patch.object(web_search_tool.account_service, "get_account", lambda token: {"email": token}),
        ):
            explicit = web_search_tool.run_web_search("explicit")
            embedded = openai_search.handle({"prompt": "embedded"})

        self.assertEqual(explicit["answer"], "explicit")
        self.assertEqual(embedded["answer"], "embedded")
        self.assertEqual(embedded["_account_email"], "B")
        self.assertEqual(selected, [set(), {"A"}, set(), {"A"}])
        self.assertEqual(marked, ["B", "B"])

    def test_expired_http_timeout_becomes_first_output_timeout(self) -> None:
        class Session:
            def post(self, *_args: object, **_kwargs: object) -> None:
                raise requests.exceptions.Timeout("request deadline")

        backend = object.__new__(OpenAIBackendAPI)
        backend.session = Session()
        backend.deadline = FirstOutputDeadline(0)
        with self.assertRaises(FirstOutputTimeout):
            backend._request("post", "https://example.test")

    def test_expired_codex_urlopen_timeout_becomes_first_output_timeout(self) -> None:
        class Deadline:
            def request_timeout(self, _timeout: float) -> float:
                return 1.0

            def is_expired(self) -> bool:
                return True

        backend = object.__new__(OpenAIBackendAPI)
        backend.access_token = "A"
        backend.base_url = "https://example.test"
        backend.deadline = Deadline()
        backend._ensure_codex_source_account = lambda: None
        backend._codex_image_input = lambda _prompt, _images: []
        backend._codex_responses_headers = lambda: {}
        backend._codex_body_preview = lambda _value, _limit: ""
        with (
            mock.patch.object(conversation_module.account_service, "get_account", return_value={}),
            mock.patch.object(conversation_module.account_service, "_decode_jwt_payload", return_value={}),
            mock.patch("services.openai_backend_api.urllib.request.urlopen", side_effect=TimeoutError("connect")) as urlopen,
        ):
            with self.assertRaises(FirstOutputTimeout):
                list(backend.iter_codex_image_response_events("draw"))
        urlopen.assert_called_once()

    def test_image_poll_deadline_raises_first_output_timeout(self) -> None:
        backend = object.__new__(OpenAIBackendAPI)
        backend.deadline = FirstOutputDeadline(0)
        with self.assertRaises(FirstOutputTimeout):
            backend._poll_image_results("conversation", timeout_secs=300)


if __name__ == "__main__":
    unittest.main()
