# Repository layer

Repositories encapsulate all **data access** for an entity. They talk to the database (via SQLAlchemy models) and return model instances. No business logic here—only queries and persistence.

**Flow:** Routes → Services → Repositories → Models (DB)

- **Routes**: HTTP, validation, response shape.
- **Services**: Business logic, orchestration, serialization (e.g. `to_dict`).
- **Repositories**: `find_all()`, `find_by_id()`, `add()`, `create()`, etc. No `db` or `Model.query` in services.

## Adding a new entity

1. Add the model in `app/models.py`.
2. Add a repository in `app/repositories/<entity>_repository.py` with `find_*` / `add` / `create` as needed.
3. Export it from `app/repositories/__init__.py`.
4. Add a service in `app/services/` that uses the repository and exposes `to_dict` (or similar).
5. Add routes that call the service.
