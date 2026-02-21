"""Unit tests for AttributeService using a fake repository."""

import pytest
from app.services import AttributeService
from app.repositories import AttributeRepository


class FakeAttribute:
    """Minimal attribute-like object for service tests."""

    def __init__(self, id="id-1", name="Color", code="color", status="active", usage_count=0):
        self.id = id
        self.name = name
        self.code = code
        self.status = status
        self.usage_count = usage_count


class FakeAttributeRepository:
    """In-memory fake for AttributeRepository."""

    def __init__(self):
        self._attributes = []

    def find_all(self, page=None, per_page=None):
        return list(self._attributes)

    def add(self, attr):
        self._attributes.append(attr)
        return attr


def test_list_all_empty():
    """list_all returns (empty list, 0) when repo has no attributes."""
    fake_repo = FakeAttributeRepository()
    service = AttributeService(fake_repo)
    items, total = service.list_all()
    assert items == []
    assert total == 0


def test_list_all_returns_repo_results():
    """list_all returns (items, total) from repository."""
    fake_repo = FakeAttributeRepository()
    fake_repo.add(FakeAttribute(id="1", name="Color", code="color"))
    fake_repo.add(FakeAttribute(id="2", name="Size", code="size"))
    service = AttributeService(fake_repo)
    items, total = service.list_all()
    assert len(items) == 2
    assert total == 2
    assert items[0].name == "Color"
    assert items[1].name == "Size"


def test_to_dict_returns_none_for_none():
    """to_dict returns None when given None."""
    fake_repo = FakeAttributeRepository()
    service = AttributeService(fake_repo)
    assert service.to_dict(None) is None


def test_to_dict_camel_case_usage_count():
    """to_dict returns usageCount (camelCase)."""
    fake_repo = FakeAttributeRepository()
    service = AttributeService(fake_repo)
    attr = FakeAttribute(id="1", name="Color", code="color", usage_count=5)
    d = service.to_dict(attr)
    assert d["usageCount"] == 5
    assert d["id"] == "1"
    assert d["name"] == "Color"
    assert d["code"] == "color"
    assert d["status"] == "active"
