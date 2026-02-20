# my-ex-master-data-service

Master Data microservice for Experience Review platform. **Python + Flask.**

## Stack

- Python 3.12
- Flask
- Flask-SQLAlchemy + PostgreSQL (psycopg2)
- Flask-Migrate (Alembic) — DB migrations
- Gunicorn (production)

## Endpoints

- `GET /health` — health check
- `GET /categories` — list categories
- `GET /categories/<id>` — get category
- `POST /categories` — create category (body: `name`, `slug`, `status`)

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

## Env vars

| Variable     | Default        | Description   |
|-------------|----------------|---------------|
| PORT        | 3004           | Server port   |
| DB_HOST     | localhost      | Postgres host |
| DB_PORT     | 5432           | Postgres port |
| DB_USER     | postgres       | DB user       |
| DB_PASSWORD | postgres       | DB password   |
| DB_NAME     | master_data_db | Database name |
