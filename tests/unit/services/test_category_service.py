"""Unit tests for CategoryService using a fake repository."""

import pytest
from app.services import CategoryService
from app.repositories import CategoryRepository


class FakeCategory:
    """Minimal category-like object for service tests."""

    def __init__(self, id="id-1", name="Cars", slug="cars", product_count=0, status="active"):
        self.id = id
        self.name = name
        self.slug = slug
        self.product_count = product_count
        self.status = status


class FakeCategoryRepository:
    """In-memory fake for CategoryRepository."""

    def __init__(self):
        self._categories = []

    def find_all(self, page=None, per_page=None):
        return list(self._categories)

    def find_by_id(self, id_):
        for c in self._categories:
            if c.id == id_:
                return c
        return None

    def create(self, id_=None, name="", slug="", status="active"):
        cat = FakeCategory(id=id_ or "generated", name=name, slug=slug, product_count=0, status=status)
        self._categories.append(cat)
        return cat


def test_list_all_empty():
    """list_all returns (empty list, 0) when repo has no categories."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    items, total = service.list_all()
    assert items == []
    assert total == 0


def test_list_all_returns_repo_results():
    """list_all returns (items, total) from repository."""
    fake_repo = FakeCategoryRepository()
    fake_repo.create(name="Cars", slug="cars")
    fake_repo.create(name="Food", slug="food")
    service = CategoryService(fake_repo)
    items, total = service.list_all()
    assert len(items) == 2
    assert total == 2
    assert items[0].name == "Cars"
    assert items[1].name == "Food"


def test_get_by_id_returns_none_when_missing():
    """get_by_id returns None when repo returns None."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    assert service.get_by_id("missing") is None


def test_get_by_id_returns_category():
    """get_by_id returns the category from repo."""
    fake_repo = FakeCategoryRepository()
    fake_repo.create(id_="cat-1", name="Phones", slug="phones")
    service = CategoryService(fake_repo)
    cat = service.get_by_id("cat-1")
    assert cat is not None
    assert cat.name == "Phones"


def test_create_normalizes_slug():
    """create derives slug from name when slug not provided."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    service.create(name="Hello World", status="active")
    assert len(fake_repo._categories) == 1
    assert fake_repo._categories[0].slug == "hello-world"


def test_create_uses_explicit_slug():
    """create uses provided slug."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    service.create(name="Cars", slug="vehicles", status="active")
    assert fake_repo._categories[0].slug == "vehicles"


def test_create_returns_created_category():
    """create returns the category returned by repo."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    cat = service.create(name="Food", slug="food")
    assert cat.name == "Food"
    assert cat.slug == "food"


def test_to_dict_returns_none_for_none():
    """to_dict returns None when given None."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    assert service.to_dict(None) is None


def test_to_dict_snake_case():
    """to_dict returns snake_case keys by default."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    cat = FakeCategory(id="1", name="Cars", slug="cars", product_count=42, status="active")
    d = service.to_dict(cat, camel_case=False)
    assert d["product_count"] == 42
    assert "productCount" not in d


def test_to_dict_camel_case():
    """to_dict with camel_case=True returns productCount."""
    fake_repo = FakeCategoryRepository()
    service = CategoryService(fake_repo)
    cat = FakeCategory(id="1", name="Cars", slug="cars", product_count=42, status="active")
    d = service.to_dict(cat, camel_case=True)
    assert d["productCount"] == 42
    assert "product_count" not in d
    assert d["id"] == "1"
    assert d["name"] == "Cars"
