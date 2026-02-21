"""Business logic for attribute operations (master data for admin). Uses AttributeRepository for data access."""

from app.repositories import AttributeRepository


class AttributeService:
    """Application service for attributes. Orchestrates repository and serialization."""

    @staticmethod
    def list_all():
        return AttributeRepository.find_all()

    @staticmethod
    def to_dict(attr):
        if not attr:
            return None
        return {
            "id": attr.id,
            "name": attr.name,
            "code": attr.code,
            "status": attr.status,
            "usageCount": attr.usage_count or 0,
        }
