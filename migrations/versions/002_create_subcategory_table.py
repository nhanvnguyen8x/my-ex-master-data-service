"""create subcategories table

Revision ID: 002
Revises: 001
Create Date: 2025-02-20

"""
from alembic import op
import sqlalchemy as sa

revision = "002"
down_revision = "001"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "subcategories",
        sa.Column("id", sa.String(50), nullable=False),
        sa.Column("category_id", sa.String(50), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("slug", sa.String(100), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["category_id"], ["categories.id"], ondelete="CASCADE"),
    )
    op.create_index("idx_subcategories_category_id", "subcategories", ["category_id"], unique=False)


def downgrade():
    op.drop_index("idx_subcategories_category_id", table_name="subcategories")
    op.drop_table("subcategories")
