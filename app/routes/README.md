# Adding a new API (route group)

Layers: **Routes → Services → Repositories → Models**. Add from the bottom up.

1. **Model** in `app/models.py`, then migration.
2. **Repository** in `app/repositories/<entity>_repository.py` (data access only). See `app/repositories/README.md`.
3. **Service** in `app/services/` that uses the repository and exposes serialization (e.g. `to_dict`).
4. **Route module** in `app/routes/`, e.g. `subcategories.py`:
   - Blueprint and route handlers that call the service.
   - Swagger docstrings.
5. **Register** in `app/routes/__init__.py`: add `(subcategories_bp, "subcategories")` to `BLUEPRINT_REGISTRY`.
6. **Swagger**: add tag in `app/__init__.py` if desired.

All registered routes are mounted under the versioned prefix (e.g. `/api/v1/...`). Change `API_V1_PREFIX` in config to adjust.
