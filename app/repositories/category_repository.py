"""Data access for categories. Services use this instead of touching models/db directly."""

import uuid
from app.models import db, Category


class CategoryRepository:
    """Repository for Category entity. Handles all persistence for categories."""

    @staticmethod
    def find_all():
        return Category.query.order_by(Category.name).all()

    @staticmethod
    def find_by_id(id_):
        return Category.query.get(id_)

    @staticmethod
    def add(category):
        db.session.add(category)
        db.session.commit()
        return category

    @staticmethod
    def create(id_=None, name="", slug="", status="active"):
        category = Category(
            id=id_ or str(uuid.uuid4()),
            name=name,
            slug=slug,
            status=status,
        )
        db.session.add(category)
        db.session.commit()
        return category
