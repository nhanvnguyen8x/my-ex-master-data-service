"""Unit tests for AttributeRepository."""

import pytest
from app.repositories import AttributeRepository


def test_find_all_empty(app):
    """find_all returns empty list when no attributes exist."""
    with app.app_context():
        repo = AttributeRepository()
        assert repo.find_all() == []


def test_create_attribute_via_model_and_find_all(app):
    """Persist an attribute (via model) and find_all returns it."""
    with app.app_context():
        from app.models import db, Attribute
        attr = Attribute(id="attr-1", name="Color", code="color", status="active", usage_count=0)
        db.session.add(attr)
        db.session.commit()
        repo = AttributeRepository()
        all_attrs = repo.find_all()
        assert len(all_attrs) == 1
        assert all_attrs[0].name == "Color"
        assert all_attrs[0].code == "color"


def test_find_all_ordered_by_name(app):
    """find_all returns attributes ordered by name."""
    with app.app_context():
        from app.models import db, Attribute
        for name, code in [("Size", "size"), ("Color", "color"), ("Brand", "brand")]:
            db.session.add(Attribute(id=code, name=name, code=code, status="active"))
        db.session.commit()
        repo = AttributeRepository()
        names = [a.name for a in repo.find_all()]
        assert names == ["Brand", "Color", "Size"]
