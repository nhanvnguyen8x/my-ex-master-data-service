from flask import Blueprint, jsonify
from sqlalchemy import text
from app import db

health_bp = Blueprint("health", __name__)


@health_bp.route("")
def health():
    """
    Liveness: process is up.
    ---
    tags:
      - Health
    responses:
      200:
        description: Service is healthy
        schema:
          type: object
          properties:
            status:
              type: string
              example: ok
            service:
              type: string
              example: my-ex-master-data-service
    """
    return jsonify({"status": "ok", "service": "my-ex-master-data-service"})


@health_bp.route("/ready")
def ready():
    """
    Readiness: DB is reachable. Use for orchestrator health checks.
    ---
    tags:
      - Health
    responses:
      200:
        description: Database is reachable
      503:
        description: Database unreachable
    """
    try:
        db.session.execute(text("SELECT 1"))
        return jsonify({"status": "ok", "database": "connected"})
    except Exception:
        return jsonify({"status": "error", "database": "disconnected"}), 503
