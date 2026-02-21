"""Business logic for attribute operations (master data for admin). Uses AttributeRepository for data access."""

from app.repositories import AttributeRepository


class AttributeService:
    """Application service for attributes. Orchestrates repository and serialization."""

    def __init__(self, attribute_repository: AttributeRepository):
        self.attribute_repository = attribute_repository

    def list_all(self, page=None, per_page=None):
        result = self.attribute_repository.find_all(page=page, per_page=per_page)
        if hasattr(result, "items"):
            return result.items, result.total
        return result, len(result)

    def to_dict(self, attr):
        if not attr:
            return None
        return {
            "id": attr.id,
            "name": attr.name,
            "code": attr.code,
            "status": attr.status,
            "usageCount": attr.usage_count or 0,
        }
