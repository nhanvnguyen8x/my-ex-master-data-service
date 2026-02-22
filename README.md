# my-ex-master-data-service

Master Data microservice for Experience Review platform. **Python + Flask.**

## Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy + PostgreSQL (psycopg2)
- Flask-Migrate (Alembic) — DB migrations
- Gunicorn (production)

## Endpoints

All APIs are versioned under `/api/v1` (configurable via `API_V1_PREFIX`):

- `GET /api/v1/health` — liveness **(no auth)**
- `GET /api/v1/health/ready` — readiness (DB check; 503 if DB down) **(no auth)**
- `GET /api/v1/categories` — list categories, paginated **(JWT required)** (`?page=1&per_page=20`; response: `{ data, meta }`, camelCase `productCount`)
- `GET /api/v1/categories/<id>` — get category **(JWT required)**
- `POST /api/v1/categories` — create category **(JWT required)** (body: `name`, `slug`, `status`)
- `GET /api/v1/tags` — list tags, paginated **(JWT required)** (`?page=1&per_page=20`; response: `{ data, meta }`)
- `GET /api/v1/attributes` — list attributes, paginated **(JWT required)** (response: `{ data, meta }`)

### Swagger UI

When the server is running, open the interactive API docs at:

**http://localhost:3004/apidocs**

Use the **Authorize** button to add a Bearer token for protected endpoints (e.g. categories). The raw OpenAPI spec is at `http://localhost:3004/apispec_1.json`.

### my-ex-admin integration

The **my-ex-admin** web app uses this service for Master Data (categories, tags, attributes). Configure the admin app:

```env
VITE_MASTER_DATA_API_URL=http://localhost:3004/api/v1
```

Then the admin will call `GET /categories`, `GET /tags`, and `GET /attributes` (relative to that base). Responses are `{ data: [...], meta: { page, per_page, total } }`; use `response.data` for the array. Categories use camelCase (`productCount`), tags and attributes use `usageCount`.

## Migrations

Migrations run **automatically when the Flask server starts** (before handling requests). No separate step is needed for deploy or Docker.

To create a new migration after changing `app/models.py`:

```bash
export FLASK_APP=wsgi:app
export DB_HOST=localhost DB_PORT=5432 DB_USER=postgres DB_PASSWORD=postgres DB_NAME=master_data_db
flask db migrate -m "describe your change"
flask db upgrade   # optional locally; production runs upgrade on start
```

## Run locally

```bash
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
export DB_HOST=localhost DB_PORT=5432 DB_USER=postgres DB_PASSWORD=postgres DB_NAME=master_data_db
python wsgi.py
```

- **`python wsgi.py`** uses port **3004** (from `PORT` env or default in code).
- **`flask run`** uses Flask’s default port **5000** unless you set **`FLASK_RUN_PORT=3004`** or copy `.env.example` to `.env` (it sets `FLASK_RUN_PORT=3004`). Then the app will be at **http://127.0.0.1:3004**.

## Docker Compose

```bash
docker compose up --build
# Service: http://localhost:3004
```

## Kubernetes

```bash
kubectl apply -f k8s/
# DB first: kubectl apply -f k8s/db-deployment.yaml
# Then: kubectl apply -f k8s/deployment.yaml k8s/service.yaml
```

## Tests

Unit tests cover the **repository** and **service** layers. Repository tests use an in-memory SQLite DB; service tests use fake repositories (no database).

**Run all unit tests:**

```bash
pip install -r requirements.txt
pytest
```

**Run with coverage:**

```bash
pytest --cov=app --cov-report=term-missing
```

**Run only repository or service tests:**

```bash
pytest tests/unit/repositories/
pytest tests/unit/services/
```

Tests are in `tests/unit/repositories/` and `tests/unit/services/`. Configuration: `pytest.ini`, `tests/conftest.py` (app fixture with `TestConfig` and SQLite).

## Adding new APIs

1. Add a new module under `app/routes/` (e.g. `subcategories.py`) with a Blueprint and route handlers.
2. Register it in `app/routes/__init__.py` by appending `(your_bp, "path-suffix")` to `BLUEPRINT_REGISTRY`.
3. Optionally add business logic in `app/services/` and keep routes thin.

See `app/routes/README.md` for details.

## Behaviour and hardening

- **Error handling:** 404/500 and unhandled exceptions return JSON `{ "error", "code", "request_id" }`; no stack traces in production.
- **Request ID:** Every request gets an `X-Request-ID` (or uses the client-provided one); it is logged and included in error responses.
- **Production guard:** If `ENV=production` (or `FLASK_ENV=production`) and `JWT_SECRET_KEY` or `SECRET_KEY` is still the default, the app raises at startup. Set real secrets before using production.
- **Validation:** `POST /categories` body is validated with Marshmallow; invalid input returns 400 with `{ "error", "code": "VALIDATION_ERROR", "details" }`.
- **Pagination:** List endpoints accept `page` and `per_page` (defaults 1 and 20, `per_page` capped at 100) and return `{ data, meta }`.
- **CORS:** Configurable via `CORS_ORIGINS` (comma-separated; default `*`).
- **Rate limiting:** 200 requests per minute per IP by default; `/health` and `/health/ready` are exempt.

## JWT validation

Protected endpoints (e.g. categories) require a valid JWT in the header:

```http
Authorization: Bearer <your-access-token>
```

Use the same **JWT_SECRET_KEY** (and algorithm) as the service that issues tokens. Health and Swagger UI are not protected.

## Env vars

| Variable                     | Default | Description                         |
|-----------------------------|--------|-------------------------------------|
| PORT                        | 3004   | Server port                         |
| API_V1_PREFIX               | /api/v1| Base path for all APIs              |
| JWT_SECRET_KEY              | (dev)  | Secret for verifying JWTs           |
| JWT_ALGORITHM               | HS256  | JWT signing algorithm               |
| JWT_ACCESS_TOKEN_EXPIRES    | 3600   | Token expiry (seconds)              |
| LOG_LEVEL                   | INFO   | Logging level (DEBUG, INFO, etc.)  |
| LOG_REQUEST_BODY_MAX_LENGTH | 2048   | Max request body chars logged       |
| LOG_RESPONSE_BODY_MAX_LENGTH| 2048   | Max response body chars logged      |
| DB_HOST                     | localhost | Postgres host                    |
| DB_PORT                     | 5432     | Postgres port                    |
| DB_USER                     | postgres | DB user                          |
| DB_PASSWORD                 | postgres | DB password                      |
| DB_NAME                     | master_data_db | Database name                 |
| CORS_ORIGINS                | *              | Comma-separated CORS origins   |
| RATELIMIT_DEFAULT           | 200 per minute | Default rate limit per IP     |
