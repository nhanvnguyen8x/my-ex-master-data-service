from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required
from app.services.attribute_service import AttributeService

attributes_bp = Blueprint("attributes", __name__)


@attributes_bp.route("", methods=["GET"])
@jwt_required()
def list_attributes():
    """
    List all attributes (master data for admin)
    ---
    tags:
      - Attributes
    security:
      - Bearer: []
    responses:
      401:
        description: Missing or invalid JWT
      200:
        description: List of attributes
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
    attributes = AttributeService.list_all()
    return jsonify([AttributeService.to_dict(a) for a in attributes])
