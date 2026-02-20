from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import Config

db = SQLAlchemy()

def create_app(config=None):
    app = Flask(__name__)
    app.config.from_object(config or Config())
    db.init_app(app)
    with app.app_context():
        from app import models  # noqa: F401
        db.create_all()
    from app.routes import health_bp, categories_bp
    app.register_blueprint(health_bp, url_prefix="/health")
    app.register_blueprint(categories_bp, url_prefix="/categories")
    return app
