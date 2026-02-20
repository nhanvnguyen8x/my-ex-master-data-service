"""initial categories table

Revision ID: 001
Revises:
Create Date: 2025-02-20

"""
from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = "001"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "categories",
        sa.Column("id", sa.String(36), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("slug", sa.String(255), nullable=True),
        sa.Column("product_count", sa.Integer(), nullable=True),
        sa.Column("status", sa.String(20), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_categories_slug"), "categories", ["slug"], unique=True)


def downgrade():
    op.drop_index(op.f("ix_categories_slug"), table_name="categories")
    op.drop_table("categories")
