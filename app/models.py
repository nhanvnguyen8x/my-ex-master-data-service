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
