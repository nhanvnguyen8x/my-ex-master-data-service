"""Global error handlers: consistent JSON error responses and no stack traces in production."""

import logging
from flask import jsonify, g

logger = logging.getLogger(__name__)


def _error_response(message: str, code: str, status: int):
    body = {"error": message, "code": code}
    request_id = g.get("request_id") if g else None
    if request_id:
        body["request_id"] = request_id
    return jsonify(body), status


def register_error_handlers(app):
    """Register 404, 500, and generic Exception handlers."""

    @app.errorhandler(404)
    def not_found(e):
        return _error_response("Not found", "NOT_FOUND", 404)

    @app.errorhandler(500)
    def internal_error(e):
        if not app.config.get("TESTING"):
            logger.exception("Internal server error")
        return _error_response(
            "Internal server error" if not app.debug else str(e),
            "INTERNAL_ERROR",
            500,
        )

    @app.errorhandler(Exception)
    def handle_exception(e):
        if not app.config.get("TESTING"):
            logger.exception("Unhandled exception: %s", e)
        # Don't leak traceback to client in production
        message = str(e) if app.debug else "Internal server error"
        return _error_response(message, "INTERNAL_ERROR", 500)
