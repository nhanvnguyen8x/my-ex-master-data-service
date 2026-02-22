from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from flasgger import Swagger
from app.config import Config

def _rate_limit_key():
    from flask import request
    path = request.path
    # Exempt: health, readiness, Swagger UI and OpenAPI spec (so docs are always reachable)
    if path.rstrip("/").endswith("health") or path.rstrip("/").endswith("ready"):
        return None
    if "/apidocs" in path or "apispec" in path:
        return None
    try:
        return get_remote_address()
    except Exception:
        return "unknown"

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
limiter = Limiter(key_func=_rate_limit_key, default_limits=["200 per minute"])

def _swagger_template(base_path):
    return {
        "swagger": "2.0",
        "info": {
            "title": "My Experience Master Data Service API",
            "description": "Versioned API for health checks and master data (categories, etc.). Protected endpoints require JWT.",
            "version": "1.0.0",
        },
        "basePath": base_path,
        "schemes": ["http", "https"],
        "securityDefinitions": {
            "Bearer": {
                "type": "apiKey",
                "name": "Authorization",
                "in": "header",
                "description": "JWT access token: Bearer &lt;token&gt;",
            },
        },
        "tags": [
            {"name": "Health", "description": "Service health check (no auth)"},
            {"name": "Categories", "description": "Category CRUD (JWT required)"},
            {"name": "Tags", "description": "Tags master data (JWT required)"},
            {"name": "Attributes", "description": "Attributes master data (JWT required)"},
        ],
    }


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config())
    from app.production_guard import check_production_config
    check_production_config(app)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    CORS(app, origins=app.config.get("CORS_ORIGINS", "*").split(","), supports_credentials=True)

    limiter.init_app(app)
    base_path = app.config.get("API_V1_PREFIX", "/api/v1")
    # Use CDN for Swagger UI so SwaggerUIBundle loads reliably (Flasgger's bundled JS can fail in browser)
    app.config.setdefault("SWAGGER", {}).update({
        "swagger_ui_bundle_js": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.52.5/swagger-ui-bundle.js",
        "swagger_ui_standalone_preset_js": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.52.5/swagger-ui-standalone-preset.js",
        "swagger_ui_css": "https://cdn.jsdelivr.net/npm/swagger-ui-dist@3.52.5/swagger-ui.css",
        "jquery_js": "https://code.jquery.com/jquery-3.7.1.min.js",
    })
    Swagger(app, template=_swagger_template(base_path))

    with app.app_context():
        from app import models  # noqa: F401
        if not app.config.get("SKIP_MIGRATIONS"):
            from flask_migrate import upgrade
            upgrade()

    from app.routes import register_blueprints
    register_blueprints(app)

    from app.request_logging import init_request_logging
    init_request_logging(app)

    from app.error_handlers import register_error_handlers
    register_error_handlers(app)

    return app
