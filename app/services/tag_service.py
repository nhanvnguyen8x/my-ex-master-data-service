"""Business logic for tag operations (master data for admin). Uses TagRepository for data access."""

from app.repositories import TagRepository


class TagService:
    """Application service for tags. Orchestrates repository and serialization."""

    def __init__(self, tag_repository: TagRepository):
        self.tag_repository = tag_repository

    def list_all(self, page=None, per_page=None):
        result = self.tag_repository.find_all(page=page, per_page=per_page)
        if hasattr(result, "items"):
            return result.items, result.total
        return result, len(result)

    def to_dict(self, tag):
        if not tag:
            return None
        return {
            "id": tag.id,
            "name": tag.name,
            "code": tag.code,
            "status": tag.status,
            "usageCount": tag.usage_count or 0,
        }
