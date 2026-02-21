"""Data access for tags. Services use this instead of touching models directly."""

from app.models import Tag


class TagRepository:
    """Repository for Tag entity."""

    @staticmethod
    def find_all():
        return Tag.query.order_by(Tag.name).all()
