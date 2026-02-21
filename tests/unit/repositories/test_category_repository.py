"""Unit tests for CategoryRepository."""

import pytest
from app.repositories import CategoryRepository


def test_find_all_empty(app):
    """find_all returns empty list when no categories exist."""
    with app.app_context():
        repo = CategoryRepository()
        assert repo.find_all() == []


def test_create_and_find_all(app):
    """create persists a category; find_all returns it."""
    with app.app_context():
        repo = CategoryRepository()
        repo.create(name="Cars", slug="cars", status="active")
        all_cats = repo.find_all()
        assert len(all_cats) == 1
        assert all_cats[0].name == "Cars"
        assert all_cats[0].slug == "cars"
        assert all_cats[0].status == "active"
        assert all_cats[0].product_count == 0


def test_create_uses_given_id(app):
    """create with id_= uses that id."""
    with app.app_context():
        repo = CategoryRepository()
        repo.create(id_="custom-id", name="Food", slug="food")
        cat = repo.find_by_id("custom-id")
        assert cat is not None
        assert cat.id == "custom-id"
        assert cat.name == "Food"


def test_find_by_id_returns_none_when_missing(app):
    """find_by_id returns None for unknown id."""
    with app.app_context():
        repo = CategoryRepository()
        assert repo.find_by_id("nonexistent") is None


def test_find_by_id_returns_category(app):
    """find_by_id returns the category when it exists."""
    with app.app_context():
        repo = CategoryRepository()
        repo.create(id_="cat-1", name="Phones", slug="phones")
        cat = repo.find_by_id("cat-1")
        assert cat is not None
        assert cat.name == "Phones"


def test_find_all_ordered_by_name(app):
    """find_all returns categories ordered by name."""
    with app.app_context():
        repo = CategoryRepository()
        repo.create(name="Zebra", slug="zebra")
        repo.create(name="Alpha", slug="alpha")
        repo.create(name="Middle", slug="middle")
        all_cats = repo.find_all()
        names = [c.name for c in all_cats]
        assert names == ["Alpha", "Middle", "Zebra"]
