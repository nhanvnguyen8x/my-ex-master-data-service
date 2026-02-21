"""Unit tests for TagRepository."""

import pytest
from app.repositories import TagRepository


def test_find_all_empty(app):
    """find_all returns empty list when no tags exist."""
    with app.app_context():
        repo = TagRepository()
        assert repo.find_all() == []


def test_create_tag_via_model_and_find_all(app):
    """Persist a tag (via model) and find_all returns it."""
    with app.app_context():
        from app.models import db, Tag
        tag = Tag(id="tag-1", name="Premium", code="prem", status="active", usage_count=0)
        db.session.add(tag)
        db.session.commit()
        repo = TagRepository()
        all_tags = repo.find_all()
        assert len(all_tags) == 1
        assert all_tags[0].name == "Premium"
        assert all_tags[0].code == "prem"


def test_find_all_ordered_by_name(app):
    """find_all returns tags ordered by name."""
    with app.app_context():
        from app.models import db, Tag
        for name, code in [("Zebra", "z"), ("Alpha", "a"), ("Beta", "b")]:
            db.session.add(Tag(id=code, name=name, code=code, status="active"))
        db.session.commit()
        repo = TagRepository()
        names = [t.name for t in repo.find_all()]
        assert names == ["Alpha", "Beta", "Zebra"]
