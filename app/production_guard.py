"""Fail or warn when running in production with unsafe default config."""

import logging
import os

logger = logging.getLogger(__name__)

UNSAFE_JWT_SECRET = "change-me-in-production"
UNSAFE_SECRET_KEY = "dev-secret"


def is_production(app):
    """Heuristic: production if ENV or FLASK_ENV is production."""
    env = os.getenv("ENV", "").lower() or os.getenv("FLASK_ENV", "").lower()
    return env == "production" or env == "prod"


def check_production_config(app):
    """Warn or raise if production and secrets are default. Skip when TESTING."""
    if app.config.get("TESTING"):
        return
    if not is_production(app):
        return
    jwt_secret = app.config.get("JWT_SECRET_KEY") or ""
    secret_key = app.config.get("SECRET_KEY") or ""
    if jwt_secret == UNSAFE_JWT_SECRET or secret_key == UNSAFE_SECRET_KEY:
        msg = (
            "Production config guard: JWT_SECRET_KEY or SECRET_KEY is still the default. "
            "Set ENV=production only after configuring real secrets."
        )
        logger.critical(msg)
        raise RuntimeError(msg)
