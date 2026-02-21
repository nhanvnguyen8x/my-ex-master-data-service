from app import db
from datetime import datetime


class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    slug = db.Column(db.String(255), unique=True, index=True)
    product_count = db.Column(db.Integer, default=0)
    status = db.Column(db.String(20), default="active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Tag(db.Model):
    __tablename__ = "tags"
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(100), nullable=True, index=True)
    status = db.Column(db.String(20), default="active")
    usage_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Attribute(db.Model):
    __tablename__ = "attributes"
    id = db.Column(db.String(36), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    code = db.Column(db.String(100), nullable=True, index=True)
    status = db.Column(db.String(20), default="active")
    usage_count = db.Column(db.Integer, default=0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
