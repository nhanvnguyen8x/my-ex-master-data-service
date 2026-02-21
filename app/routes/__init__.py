"""
Blueprint registry: add new APIs here to mount them under API_V1_PREFIX.

Each entry: (blueprint, path_suffix)
  - path_suffix is the path under the versioned API (e.g. "health" -> /api/v1/health)
"""
from app.routes.health import health_bp
from app.routes.categories import categories_bp
from app.routes.tags import tags_bp
from app.routes.attributes import attributes_bp

# Registry: (blueprint, path_suffix). Order does not affect routing.
BLUEPRINT_REGISTRY = [
    (health_bp, "health"),
    (categories_bp, "categories"),
    (tags_bp, "tags"),
    (attributes_bp, "attributes"),
]


def register_blueprints(app):
    """Register all blueprints from the registry with the app's API prefix."""
    api_prefix = app.config.get("API_V1_PREFIX", "/api/v1").rstrip("/")
    for blueprint, path_suffix in BLUEPRINT_REGISTRY:
        prefix = f"{api_prefix}/{path_suffix}"
        app.register_blueprint(blueprint, url_prefix=prefix)


__all__ = ["BLUEPRINT_REGISTRY", "register_blueprints", "health_bp", "categories_bp", "tags_bp", "attributes_bp"]
