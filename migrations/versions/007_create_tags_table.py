"""create tags table

Revision ID: 007
Revises: 006
Create Date: 2025-02-21

"""
from alembic import op
import sqlalchemy as sa

revision = "007"
down_revision = "006"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "tags",
        sa.Column("id", sa.String(36), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("code", sa.String(100), nullable=True),
        sa.Column("status", sa.String(20), nullable=True),
        sa.Column("usage_count", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_tags_code"), "tags", ["code"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_tags_code"), table_name="tags")
    op.drop_table("tags")
