from flask import Blueprint, request, jsonify
from app.models import db, Category
import uuid

categories_bp = Blueprint("categories", __name__)

@categories_bp.route("", methods=["GET"])
def list_categories():
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
