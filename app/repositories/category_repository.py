"""Data access for categories. Services use this instead of touching models/db directly."""

import uuid
from app.models import db, Category


class CategoryRepository:
    """Repository for Category entity. Handles all persistence for categories."""

    def find_all(self, page=None, per_page=None):
        q = Category.query.order_by(Category.name)
        if page is not None and per_page is not None:
            return q.paginate(page=page, per_page=per_page, error_out=False)
        return q.all()

    def find_by_id(self, id_) -> Category:
        return db.session.get(Category, id_)

    def count(self):
        return Category.query.count()

    def add(self, category):
        db.session.add(category)
        db.session.commit()
        return category

    def create(self, id_=None, name="", slug="", status="active"):
        category = Category(
            id=id_ or str(uuid.uuid4()),
            name=name,
            slug=slug,
            status=status,
        )
        db.session.add(category)
        db.session.commit()
        return category
