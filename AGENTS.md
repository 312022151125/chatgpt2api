# Repository Guidelines

## Project Overview

`chatgpt2api` is a Python 3.13 FastAPI service that exposes OpenAI- and Anthropic-compatible APIs backed by ChatGPT web/account integrations. A Next.js frontend provides admin account, image, settings, logs, and debugging UIs. The Docker image serves both API and static frontend assets.

## Architecture & Data Flow

- **Backend entrypoint:** `main.py` creates the module-level FastAPI app with `create_app()` and runs Uvicorn when invoked directly.
- **App composition:** `api/app.py` installs exception handlers and CORS, mounts routers for AI, accounts, image tasks, and system endpoints, starts background account/image/backup work in lifespan, then serves `web_dist` with SPA fallback.
- **API request flow:** frontend wrappers in `web/src/lib/api.ts` call `web/src/lib/request.ts`; Axios adds the auth key as a Bearer token and normalizes errors. Backend routes authenticate through `api/support.py`/`AuthService`, validate Pydantic DTOs, then delegate to services.
- **Protocol compatibility:** `api/ai.py` routes OpenAI Chat Completions, Responses, Anthropic Messages, image, and search requests to protocol-specific services under `services/protocol/`. Blocking upstream work is moved to `run_in_threadpool`.
- **Image tasks:** `api/image_tasks.py` validates and filters prompts, parses multipart/image inputs, and delegates asynchronous work to `services/image_task_service.py`; the frontend polls task IDs.
- **Accounts:** `api/accounts.py` owns request DTOs and route orchestration. `services/account_service.py` normalizes token-to-account state, guards mutation with locks/conditions, persists through `StorageBackend`, and logs changes.
- **Persistence:** `services/storage/factory.py` selects JSON (default), SQLite/PostgreSQL, or Git storage from `STORAGE_BACKEND` and related environment variables. `services/storage/base.py` defines the backend contract.
- **Frontend state:** Next route modules under `web/src/app/` are mostly client-heavy. Auth/session checks use `web/src/lib/use-auth-guard.ts`; settings state and normalization live in the Zustand store `web/src/app/settings/store.ts`.

## Key Directories

- `api/` — FastAPI app, routers, request DTOs, auth support, protocol endpoints.
- `services/` — account, auth, config, storage, image, backup, logging, and upstream protocol services.
- `utils/` — shared backend helpers.
- `web/src/app/` — Next.js routes and page-level UI.
- `web/src/components/` — shared frontend components.
- `web/src/lib/` — API client, request/auth helpers, formatting, and shared utilities.
- `test/` — stdlib `unittest` tests, in-process API tests, and live HTTP diagnostics.
- `scripts/` — storage migration/health checks, proxy initialization, OAuth refresh diagnostics, and mailbox tooling.
- `data/` — runtime persistence; preserve during maintenance.
- `web/` — sole JavaScript package; no root `package.json` or JS workspace.

## Development Commands

Backend:

```bash
uv sync
uv run main.py
```

Frontend development:

```bash
cd web
bun install
bun run dev
```

Frontend checks/build:

```bash
cd web
npx eslint .
npx tsc --noEmit
bun run build
```

Python tests and storage smoke check:

```bash
python -m unittest discover -s test -p 'test_*.py'
python test/test_account_export.py
python scripts/test_storage.py
```

Docker deployments:

```bash
docker compose up -d                         # published image, UI/API on port 3000
docker compose -f docker-compose.local.yml up -d  # local image, port 8000, SQLite
docker compose -f docker-compose.warp.yml up -d --build

docker compose ps
docker logs -f chatgpt2api
docker compose down
```

Storage migration examples:

```bash
python scripts/migrate_storage.py --from json --to postgres
python scripts/migrate_storage.py --export backup.json
python scripts/migrate_storage.py --import backup.json
```

## Code Conventions & Common Patterns

### Backend

- Use `from __future__ import annotations`, type annotations, snake_case names, and Pydantic `BaseModel` request/response DTOs.
- Router modules expose `create_router()` functions and keep route handlers thin.
- Authenticate and validate at the route boundary. Convert expected failures to `HTTPException` with the established status/detail shape; preserve protocol-specific response formats.
- Keep blocking I/O out of async handlers with `run_in_threadpool`.
- Reuse module-level service singletons and the existing storage/config abstractions; do not add a second service or persistence pattern for one feature.
- Protect shared account/runtime state with the existing locks/conditions. Persist through `StorageBackend`, not directly through a concrete backend.

### Frontend

- Use TypeScript with strict checking, `@/*` imports mapped to `web/src/*`, and existing React/Next client-component patterns.
- Add API calls to `web/src/lib/api.ts` and reuse `web/src/lib/request.ts` for auth/error behavior.
- Use Zustand for shared settings/runtime state; normalize and clamp values at the store boundary.
- Use `useAuthGuard` for protected pages instead of duplicating redirects/session checks.
- Reuse existing Radix, Tailwind, `cn()`, and shared UI components before creating new primitives.

## Important Files

- `main.py` — backend/Uvicorn entrypoint.
- `api/app.py` — FastAPI assembly, lifespan, router registration, static frontend serving.
- `api/ai.py` — OpenAI/Anthropic-compatible AI endpoints.
- `api/accounts.py` — account administration routes and DTOs.
- `api/image_tasks.py` — image task API.
- `services/account_service.py` — account state and persistence coordination.
- `services/config.py` — config loading, environment overrides, cached backend selection.
- `services/storage/factory.py` and `services/storage/base.py` — storage selection and contract.
- `web/src/lib/api.ts` and `web/src/lib/request.ts` — frontend/backend boundary.
- `web/src/app/settings/store.ts` — shared settings state.
- `pyproject.toml`, `uv.lock` — Python dependencies and lockfile.
- `web/package.json`, `web/tsconfig.json`, `web/next.config.ts` — frontend scripts and build behavior.
- `Dockerfile` — multi-stage frontend build and Python runtime image.
- `docker-compose*.yml`, `.env.example` — runtime/storage/proxy deployment configuration.
- `.github/workflows/docker-publish.yml` — GHCR multi-architecture publish workflow.

## Runtime/Tooling Preferences

- Python **>=3.13**, managed with `uv`; production runs `uvicorn` from the uv environment.
- Frontend is Next.js 16 / React 19 / TypeScript. Local documentation prefers **Bun** for install and development.
- Docker frontend build uses Node 22 Alpine and currently runs plain `npm install`; it copies `web/bun.lock` but not `web/package-lock.json`, so dependency installation is not lockfile-reproducible. Do not assume Docker and local dependency resolution are identical.
- Next is configured for static export (`output: 'export'`) with unoptimized images and trailing slashes. Build output is `web/out/`, copied into `/app/web_dist`.
- `next.config.ts` sets `typescript.ignoreBuildErrors: true`; run `npx tsc --noEmit` separately when validating frontend changes.
- Main configuration comes from `config.json` plus environment overrides. Important variables include `CHATGPT2API_AUTH_KEY`, `CHATGPT2API_BASE_URL`, `STORAGE_BACKEND`, `DATABASE_URL`, `GIT_REPO_URL`, `GIT_TOKEN`, and proxy runtime variables documented in `.env.example`.
- Default published Compose uses JSON storage and port 3000. Local Compose uses SQLite and port 8000.

## Testing & QA

- Python tests use stdlib `unittest`, not pytest. Files are `test/test_*.py`; classes commonly end in `Tests`; methods use `test_<behavior>`.
- In-process FastAPI tests use `fastapi.testclient.TestClient`, local fake services, `unittest.mock`, and temporary directories. Assert observable status codes, payloads, service calls, persistence, and error boundaries.
- Live HTTP tests under `test/test_v1_*.py` require a running app on port 8000 plus valid configured accounts/upstream access. Treat them as integration diagnostics, not hermetic unit tests.
- `scripts/test_storage.py` temporarily writes a test account, verifies health/read/write/reload, then restores original data. Run only against an intended storage target and keep backups for important data.
- No coverage threshold, Python lint/typecheck/format configuration, frontend test script, or CI test/lint gate is configured. Frontend lint and typecheck are direct commands, not package scripts.
- CI currently builds and pushes `linux/amd64` and `linux/arm64` images to GHCR on `main` pushes or manual dispatch; it does not run tests.
- Before changing persistence or deployment behavior, check `config.json`, `.env.example`, the relevant Compose file, and `services/config.py` together. Preserve `data/`, `config.json`, and `.env` during upgrades or rollback.
