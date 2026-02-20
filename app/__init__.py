from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger
from app.config import Config

db = SQLAlchemy()
migrate = Migrate()

SWAGGER_TEMPLATE = {
    "swagger": "2.0",
    "info": {
        "title": "My Experience Master Data Service API",
        "description": "API for health checks and category master data",
        "version": "1.0.0",
    },
    "basePath": "/",
    "schemes": ["http", "https"],
    "tags": [
        {"name": "Health", "description": "Service health check"},
        {"name": "Categories", "description": "Category CRUD operations"},
    ],
}


def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config())
    db.init_app(app)
    migrate.init_app(app, db)
    Swagger(app, template=SWAGGER_TEMPLATE)

    with app.app_context():
        from app import models  # noqa: F401
        from flask_migrate import upgrade
        upgrade()

    from app.routes import health_bp, categories_bp
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    return app
