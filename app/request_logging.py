"""
Request/response logging: logs request method, path, query params, body and response status, body.
Sensitive headers (e.g. Authorization) are masked.
"""

import logging
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


def _mask_headers(headers: dict) -> dict:
    out = dict(headers)
    if "Authorization" in out:
        val = out["Authorization"]
        if val and val.lower().startswith("bearer "):
            out["Authorization"] = "Bearer ***"
        else:
            out["Authorization"] = "***"
    return out


def init_request_logging(app):
    """Register before_request and after_request to log request params, body and response body."""
    logger = logging.getLogger("app.request")
    logger.setLevel(getattr(logging, app.config.get("LOG_LEVEL", "INFO").upper(), logging.INFO))
    if not logger.handlers:
        handler = logging.StreamHandler()
        handler.setFormatter(
            logging.Formatter("%(asctime)s [%(levelname)s] %(name)s: %(message)s")
        )
        logger.addHandler(handler)

    req_max = app.config.get("LOG_REQUEST_BODY_MAX_LENGTH", 2048)
    res_max = app.config.get("LOG_RESPONSE_BODY_MAX_LENGTH", 2048)

    @app.before_request
    def log_request():
        # Ensure request body is cached so the view can still read it
        body = request.get_data(cache=True)
        query = dict(request.args) if request.args else None
        headers = _mask_headers(dict(request.headers))
        logger.info(
            "Request: %s %s | query=%s | headers=%s | body=%s",
            request.method,
            request.path,
            query,
            headers,
            _safe_body(body, req_max),
        )
        g._request_body_logged = True

    @app.after_request
    def log_response(response):
        body = response.get_data()
        response_body = _safe_body(body, res_max)
        logger.info(
            "Response: %s %s | status=%s | body=%s",
            request.method,
            request.path,
            response.status_code,
            response_body,
        )
        return response
