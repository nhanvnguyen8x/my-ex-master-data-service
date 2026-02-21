from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError as MarshmallowValidationError
from app.container import category_service
from app.schemas import CreateCategorySchema

categories_bp = Blueprint("categories", __name__)
create_category_schema = CreateCategorySchema()


def _parse_pagination():
    page = max(1, int(request.args.get("page", 1)))
    per_page = min(100, max(1, int(request.args.get("per_page", 20))))
    return page, per_page


@categories_bp.route("", methods=["GET"])
@jwt_required()
def list_categories():
    """
    List all categories (paginated)
    ---
    tags:
      - Categories
    security:
      - Bearer: []
    parameters:
      - name: page
        in: query
        type: integer
        default: 1
      - name: per_page
        in: query
        type: integer
        default: 20
    responses:
      401:
        description: Missing or invalid JWT
      200:
        description: List of categories with pagination meta
    """
    page, per_page = _parse_pagination()
    items, total = category_service.list_all(page=page, per_page=per_page)
    return jsonify({
        "data": [category_service.to_dict(c, camel_case=True) for c in items],
        "meta": {"page": page, "per_page": per_page, "total": total},
    })


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
    category = category_service.get_by_id(id)
    if not category:
        return jsonify({"error": "Not found"}), 404
    return jsonify(category_service.to_dict(category, camel_case=True))


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
    raw = request.get_json() or {}
    try:
        data = create_category_schema.load(raw)
    except MarshmallowValidationError as e:
        return jsonify({"error": "Validation failed", "code": "VALIDATION_ERROR", "details": e.messages}), 400
    category = category_service.create(
        name=data["name"],
        slug=data.get("slug"),
        status=data.get("status", "active"),
    )
    return jsonify(category_service.to_dict(category, camel_case=True)), 201
