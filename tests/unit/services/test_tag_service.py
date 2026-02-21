"""Unit tests for TagService using a fake repository."""

import pytest
from app.services import TagService
from app.repositories import TagRepository


class FakeTag:
    """Minimal tag-like object for service tests."""

    def __init__(self, id="id-1", name="Premium", code="prem", status="active", usage_count=0):
        self.id = id
        self.name = name
        self.code = code
        self.status = status
        self.usage_count = usage_count


class FakeTagRepository:
    """In-memory fake for TagRepository."""

    def __init__(self):
        self._tags = []

    def find_all(self, page=None, per_page=None):
        return list(self._tags)

    def add(self, tag):
        self._tags.append(tag)
        return tag


def test_list_all_empty():
    """list_all returns (empty list, 0) when repo has no tags."""
    fake_repo = FakeTagRepository()
    service = TagService(fake_repo)
    items, total = service.list_all()
    assert items == []
    assert total == 0


def test_list_all_returns_repo_results():
    """list_all returns (items, total) from repository."""
    fake_repo = FakeTagRepository()
    fake_repo.add(FakeTag(id="1", name="Premium", code="prem"))
    fake_repo.add(FakeTag(id="2", name="Sale", code="sale"))
    service = TagService(fake_repo)
    items, total = service.list_all()
    assert len(items) == 2
    assert total == 2
    assert items[0].name == "Premium"
    assert items[1].name == "Sale"


def test_to_dict_returns_none_for_none():
    """to_dict returns None when given None."""
    fake_repo = FakeTagRepository()
    service = TagService(fake_repo)
    assert service.to_dict(None) is None


def test_to_dict_camel_case_usage_count():
    """to_dict returns usageCount (camelCase)."""
    fake_repo = FakeTagRepository()
    service = TagService(fake_repo)
    tag = FakeTag(id="1", name="Tag", code="t", usage_count=10)
    d = service.to_dict(tag)
    assert d["usageCount"] == 10
    assert d["id"] == "1"
    assert d["name"] == "Tag"
    assert d["code"] == "t"
    assert d["status"] == "active"
