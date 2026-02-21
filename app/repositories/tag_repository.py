"""Data access for tags. Services use this instead of touching models directly."""

from app.models import Tag


class TagRepository:
    """Repository for Tag entity."""

    def find_all(self, page=None, per_page=None):
        q = Tag.query.order_by(Tag.name)
        if page is not None and per_page is not None:
            return q.paginate(page=page, per_page=per_page, error_out=False)
        return q.all()

    def count(self):
        return Tag.query.count()
