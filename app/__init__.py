from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flasgger import Swagger
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

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
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    base_path = app.config.get("API_V1_PREFIX", "/api/v1")
    Swagger(app, template=_swagger_template(base_path))

    with app.app_context():
        from app import models  # noqa: F401
        from flask_migrate import upgrade
        upgrade()

    from app.routes import register_blueprints
    register_blueprints(app)

    from app.request_logging import init_request_logging
    init_request_logging(app)

    return app
