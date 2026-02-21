"""Data access for attributes. Services use this instead of touching models directly."""

from app.models import Attribute


class AttributeRepository:
    """Repository for Attribute entity."""

    def find_all(self, page=None, per_page=None):
        q = Attribute.query.order_by(Attribute.name)
        if page is not None and per_page is not None:
            return q.paginate(page=page, per_page=per_page, error_out=False)
        return q.all()

    def count(self):
        return Attribute.query.count()
