from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.tag_service import TagService

tags_bp = Blueprint("tags", __name__)


@tags_bp.route("", methods=["GET"])
@jwt_required()
def list_tags():
    """
    List all tags (master data for admin)
    ---
    tags:
      - Tags
    security:
      - Bearer: []
    responses:
      401:
        description: Missing or invalid JWT
      200:
        description: List of tags
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
              name:
                type: string
              code:
                type: string
              status:
                type: string
              usageCount:
                type: integer
    """
    tags = TagService.list_all()
    return jsonify([TagService.to_dict(t) for t in tags])
