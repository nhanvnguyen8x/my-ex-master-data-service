from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.container import attribute_service

attributes_bp = Blueprint("attributes", __name__)


def _parse_pagination():
    page = max(1, int(request.args.get("page", 1)))
    per_page = min(100, max(1, int(request.args.get("per_page", 20))))
    return page, per_page


@attributes_bp.route("", methods=["GET"])
@jwt_required()
def list_attributes():
    """
    List all attributes (paginated)
    ---
    tags:
      - Attributes
    security:
      - Bearer: []
    parameters:
      - name: page
        in: query
        type: integer
      - name: per_page
        in: query
        type: integer
    responses:
      401:
        description: Missing or invalid JWT
      200:
        description: List of attributes with pagination meta
    """
    page, per_page = _parse_pagination()
    items, total = attribute_service.list_all(page=page, per_page=per_page)
    return jsonify({
        "data": [attribute_service.to_dict(a) for a in items],
        "meta": {"page": page, "per_page": per_page, "total": total},
    })
