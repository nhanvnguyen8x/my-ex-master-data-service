from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from app.services import CategoryService

categories_bp = Blueprint("categories", __name__)


@categories_bp.route("", methods=["GET"])
@jwt_required()
def list_categories():
    """
    List all categories
    ---
    tags:
      - Categories
    security:
      - Bearer: []
    responses:
      401:
        description: Missing or invalid JWT
      200:
        description: List of categories
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: string
                format: uuid
              name:
                type: string
              slug:
                type: string
              product_count:
                type: integer
              status:
                type: string
                enum: [active, inactive]
    """
    categories = CategoryService.list_all()
    return jsonify([CategoryService.to_dict(c, camel_case=True) for c in categories])


@categories_bp.route("/<id>", methods=["GET"])
@jwt_required()
def get_category(id):
    """
    Get a category by ID
    ---
    tags:
      - Categories
    security:
      - Bearer: []
    parameters:
      - name: id
        in: path
        type: string
        required: true
        description: Category UUID
    responses:
      200:
        description: Category details
        schema:
          type: object
          properties:
            id:
              type: string
              format: uuid
            name:
              type: string
            slug:
              type: string
            product_count:
              type: integer
            status:
              type: string
      404:
        description: Category not found
        schema:
          type: object
          properties:
            error:
              type: string
              example: Not found
    """
    category = CategoryService.get_by_id(id)
    if not category:
        return jsonify({"error": "Not found"}), 404
    return jsonify(CategoryService.to_dict(category, camel_case=True))


@categories_bp.route("", methods=["POST"])
@jwt_required()
def create_category():
    """
    Create a new category
    ---
    tags:
      - Categories
    security:
      - Bearer: []
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
              description: Category name
            slug:
              type: string
              description: URL-friendly slug (optional, derived from name if omitted)
            status:
              type: string
              enum: [active, inactive]
              default: active
    responses:
      201:
        description: Category created
        schema:
          type: object
          properties:
            id:
              type: string
              format: uuid
            name:
              type: string
            slug:
              type: string
            product_count:
              type: integer
            status:
              type: string
    """
    data = request.get_json() or {}
    category = CategoryService.create(
        name=data.get("name", ""),
        slug=data.get("slug"),
        status=data.get("status", "active"),
    )
    return jsonify(CategoryService.to_dict(category, camel_case=True)), 201
