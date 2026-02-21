# Repository layer

Repositories encapsulate all **data access** for an entity. They use **instance methods** (no `@staticmethod`) and talk to the database via SQLAlchemy models. No business logic—only queries and persistence.

**Flow:** Routes → Services → Repositories → Models (DB)

- **Routes**: Import services from `app.container`, call instance methods.
- **Services**: Take a repository in `__init__` (dependency injection); business logic and serialization.
- **Repositories**: Instance methods like `find_all()`, `find_by_id()`, `create()`. No `db` or `Model.query` in services.

## Adding a new entity

1. Add the model in `app/models.py`.
2. Add a repository in `app/repositories/<entity>_repository.py` with `find_*` / `add` / `create` as needed.
3. Export it from `app/repositories/__init__.py`.
4. Add a service in `app/services/` that uses the repository and exposes `to_dict` (or similar).
5. Add routes that call the service.
