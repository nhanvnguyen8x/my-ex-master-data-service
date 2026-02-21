from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.container import tag_service

tags_bp = Blueprint("tags", __name__)


def _parse_pagination():
    page = max(1, int(request.args.get("page", 1)))
    per_page = min(100, max(1, int(request.args.get("per_page", 20))))
    return page, per_page


@tags_bp.route("", methods=["GET"])
@jwt_required()
def list_tags():
    """
    List all tags (paginated)
    ---
    tags:
      - Tags
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
        description: List of tags with pagination meta
    """
    page, per_page = _parse_pagination()
    items, total = tag_service.list_all(page=page, per_page=per_page)
    return jsonify({
        "data": [tag_service.to_dict(t) for t in items],
        "meta": {"page": page, "per_page": per_page, "total": total},
    })
