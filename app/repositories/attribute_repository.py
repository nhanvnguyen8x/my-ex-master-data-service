"""Data access for attributes. Services use this instead of touching models directly."""

from app.models import Attribute


class AttributeRepository:
    """Repository for Attribute entity."""

    @staticmethod
    def find_all():
        return Attribute.query.order_by(Attribute.name).all()
