"""Pytest fixtures for app context and test DB."""

import pytest
from app import create_app, db
from app.config import TestConfig


@pytest.fixture(scope="function")
def app():
    """Create app with TestConfig (SQLite in-memory, no migrations)."""
    application = create_app(TestConfig())
    with application.app_context():
        db.create_all()
    yield application
    with application.app_context():
        db.drop_all()


@pytest.fixture(scope="function")
def app_context(app):
    """Active app context for a test."""
    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def db_session(app):
    """Run test in a transaction and rollback after (isolation)."""
    with app.app_context():
        connection = db.engine.connect()
        transaction = connection.begin()
        yield db.session
        transaction.rollback()
        connection.close()
