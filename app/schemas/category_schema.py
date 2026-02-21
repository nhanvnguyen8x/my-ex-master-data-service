"""Request validation for category endpoints."""

from marshmallow import Schema, fields, validate, ValidationError


class CreateCategorySchema(Schema):
    name = fields.String(required=True, validate=validate.Length(min=1, max=255))
    slug = fields.String(load_default=None, allow_none=True, validate=validate.Length(max=255))
    status = fields.String(load_default="active", validate=validate.OneOf(["active", "inactive"]))
