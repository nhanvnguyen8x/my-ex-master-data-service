"""Business logic for category operations. Uses CategoryRepository for data access."""

from app.repositories import CategoryRepository


class CategoryService:
    """Application service for categories. Orchestrates repository and serialization."""

    def __init__(self, category_repository: CategoryRepository):
        self.category_repository = category_repository

    def list_all(self, page=None, per_page=None):
        result = self.category_repository.find_all(page=page, per_page=per_page)
        if hasattr(result, "items"):
            return result.items, result.total
        return result, len(result)

    def get_by_id(self, id_):
        return self.category_repository.find_by_id(id_)

    def create(self, name, slug=None, status="active"):
        slug = (slug or name or "").lower().replace(" ", "-")
        return self.category_repository.create(name=name or "", slug=slug, status=status)

    def to_dict(self, category, camel_case=False):
        if not category:
            return None
        data = {
            "id": category.id,
            "name": category.name,
            "slug": category.slug,
            "product_count": category.product_count,
            "status": category.status,
        }
        if camel_case:
            data["productCount"] = data.pop("product_count", category.product_count)
        return data
