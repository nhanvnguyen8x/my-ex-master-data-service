"""Business logic for category operations. Uses CategoryRepository for data access."""

from app.repositories import CategoryRepository


class CategoryService:
    """Application service for categories. Orchestrates repository and serialization."""

    @staticmethod
    def list_all():
        return CategoryRepository.find_all()

    @staticmethod
    def get_by_id(id_):
        return CategoryRepository.find_by_id(id_)

    @staticmethod
    def create(name, slug=None, status="active"):
        slug = (slug or name or "").lower().replace(" ", "-")
        return CategoryRepository.create(name=name or "", slug=slug, status=status)

    @staticmethod
    def to_dict(category, camel_case=False):
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
