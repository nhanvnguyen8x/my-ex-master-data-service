"""
Request/response logging: request params (method, path, query), body when present, response status; body on error; exceptions in error_handlers.
"""

import logging
import uuid
from flask import request, g


def _truncate(s: str, max_length: int) -> str:
    if not s or len(s) <= max_length:
        return s or ""
    return s[:max_length] + f"... (truncated, total {len(s)} chars)"


def _safe_body(data: bytes, max_length: int) -> str:
    if not data:
        return ""
    try:
        text = data.decode("utf-8", errors="replace")
    except Exception:
        return "<binary or undecodable>"
    return _truncate(text, max_length)


class RequestIdFilter(logging.Filter):
    """Add request_id from Flask g to log records."""

    def filter(self, record):
        record.request_id = getattr(g, "request_id", None) or "-"
        return True


def init_request_logging(app):
    """Register request ID, before_request and after_request logging."""
    logger = logging.getLogger("app.request")
    logger.setLevel(getattr(logging, app.config.get("LOG_LEVEL", "INFO").upper(), logging.INFO))
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.addFilter(RequestIdFilter())
        handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s] %(name)s [%(request_id)s]: %(message)s"
            )
        )
        logger.addHandler(handler)

    req_max = app.config.get("LOG_REQUEST_BODY_MAX_LENGTH", 2048)
    res_max = app.config.get("LOG_RESPONSE_BODY_MAX_LENGTH", 2048)

    @app.before_request
    def set_request_id_and_log():
        g.request_id = request.headers.get("X-Request-ID") or str(uuid.uuid4())
        body = request.get_data(cache=True)
        body_str = _safe_body(body, req_max)
        parts = ["Request: %s %s" % (request.method, request.path)]
        if request.query_string:
            parts.append("query=%s" % request.query_string.decode("utf-8", errors="replace"))
        if body_str:
            parts.append("body=%s" % body_str)
        logger.info(" | ".join(parts))

    @app.after_request
    def log_response_and_add_request_id(response):
        if g.get("request_id"):
            response.headers["X-Request-ID"] = g.request_id
        parts = ["Response: %s %s | status=%s" % (request.method, request.path, response.status_code)]
        if response.status_code >= 400:
            body = response.get_data()
            body_str = _safe_body(body, res_max)
            if body_str:
                parts.append("body=%s" % body_str)
        logger.info(" | ".join(parts))
        return response
