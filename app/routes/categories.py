from flask import Blueprint, request, jsonify
from app.models import db, Category
import uuid

categories_bp = Blueprint("categories", __name__)


@categories_bp.route("", methods=["GET"])
def list_categories():
    """
    List all categories
    ---
    tags:
      - Categories
    responses:
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
    categories = Category.query.order_by(Category.name).all()
    return jsonify([{
        "id": c.id,
        "name": c.name,
        "slug": c.slug,
        "product_count": c.product_count,
        "status": c.status,
    } for c in categories])


@categories_bp.route("/<id>", methods=["GET"])
def get_category(id):
    """
    Get a category by ID
    ---
    tags:
      - Categories
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
    c = Category.query.get(id)
    if not c:
        return jsonify({"error": "Not found"}), 404
    return jsonify({
        "id": c.id,
        "name": c.name,
        "slug": c.slug,
        "product_count": c.product_count,
        "status": c.status,
    })


@categories_bp.route("", methods=["POST"])
def create_category():
    """
    Create a new category
    ---
    tags:
      - Categories
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
    cat = Category(
        id=str(uuid.uuid4()),
        name=data.get("name", ""),
        slug=data.get("slug", "").lower().replace(" ", "-"),
        status=data.get("status", "active"),
    )
    db.session.add(cat)
    db.session.commit()
    return jsonify({
        "id": cat.id,
        "name": cat.name,
        "slug": cat.slug,
        "product_count": cat.product_count,
        "status": cat.status,
    }), 201
