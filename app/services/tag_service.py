"""Business logic for tag operations (master data for admin). Uses TagRepository for data access."""

from app.repositories import TagRepository


class TagService:
    """Application service for tags. Orchestrates repository and serialization."""

    @staticmethod
    def list_all():
        return TagRepository.find_all()

    @staticmethod
    def to_dict(tag):
        if not tag:
            return None
        return {
            "id": tag.id,
            "name": tag.name,
            "code": tag.code,
            "status": tag.status,
            "usageCount": tag.usage_count or 0,
        }
