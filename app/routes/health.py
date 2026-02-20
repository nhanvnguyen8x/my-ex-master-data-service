from flask import Blueprint, jsonify

health_bp = Blueprint("health", __name__)


@health_bp.route("")
def health():
    """
    Health check endpoint
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
