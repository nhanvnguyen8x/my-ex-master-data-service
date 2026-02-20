"""create products table

Revision ID: 003
Revises: 002
Create Date: 2025-02-20

"""
from alembic import op
import sqlalchemy as sa

revision = "003"
down_revision = "002"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "products",
        sa.Column("id", sa.String(50), nullable=False),
        sa.Column("subcategory_id", sa.String(50), nullable=False),
        sa.Column("name", sa.String(100), nullable=False),
        sa.Column("slug", sa.String(100), nullable=False),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["subcategory_id"], ["subcategories.id"], ondelete="CASCADE"),
    )
    op.create_index("idx_products_subcategory_id", "products", ["subcategory_id"], unique=False)


def downgrade():
    op.drop_index("idx_products_subcategory_id", table_name="products")
    op.drop_table("products")
