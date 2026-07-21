from __future__ import annotations

from services.account_service import account_service
from services.openai_backend_api import SEARCH_MODEL
from services.protocol.web_search_tool import _run_web_search_with_account

MODEL = SEARCH_MODEL


def handle(body: dict[str, object]) -> dict[str, object]:
    result, token = _run_web_search_with_account(str(body["prompt"]))
    account = account_service.get_account(token) or {}
    result["_account_email"] = str(account.get("email") or "")
    return result
