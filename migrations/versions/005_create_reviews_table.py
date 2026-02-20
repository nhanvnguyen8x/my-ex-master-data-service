"""create reviews table

Revision ID: 005
Revises: 004
Create Date: 2025-02-20

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects.postgresql import UUID

revision = "005"
down_revision = "004"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "reviews",
        sa.Column("id", UUID(as_uuid=True), server_default=sa.text("gen_random_uuid()"), nullable=False),
        sa.Column("user_id", UUID(as_uuid=True), nullable=True),
        sa.Column("category_id", sa.String(50), nullable=False),
        sa.Column("subcategory_id", sa.String(50), nullable=True),
        sa.Column("product_id", sa.String(50), nullable=True),
        sa.Column("year", sa.SmallInteger(), nullable=True),
        sa.Column("title", sa.String(255), nullable=False),
        sa.Column("body", sa.Text(), nullable=False),
        sa.Column("rating", sa.SmallInteger(), nullable=True),
        sa.Column("created_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=True),
        sa.Column("updated_at", sa.DateTime(), server_default=sa.text("CURRENT_TIMESTAMP"), nullable=True),
        sa.PrimaryKeyConstraint("id"),
        sa.ForeignKeyConstraint(["user_id"], ["users.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["category_id"], ["categories.id"], ondelete="CASCADE"),
        sa.ForeignKeyConstraint(["subcategory_id"], ["subcategories.id"], ondelete="SET NULL"),
        sa.ForeignKeyConstraint(["product_id"], ["products.id"], ondelete="SET NULL"),
        sa.CheckConstraint("rating >= 1 AND rating <= 5", name="reviews_rating_check"),
    )
    op.create_index("idx_reviews_category_id", "reviews", ["category_id"], unique=False)
    op.create_index("idx_reviews_subcategory_id", "reviews", ["subcategory_id"], unique=False)
    op.create_index("idx_reviews_product_id", "reviews", ["product_id"], unique=False)
    op.create_index("idx_reviews_year", "reviews", ["year"], unique=False)
    op.create_index("idx_reviews_created_at", "reviews", ["created_at"], unique=False)
    op.create_index("idx_reviews_user_id", "reviews", ["user_id"], unique=False)


def downgrade():
    op.drop_index("idx_reviews_user_id", table_name="reviews")
    op.drop_index("idx_reviews_created_at", table_name="reviews")
    op.drop_index("idx_reviews_year", table_name="reviews")
    op.drop_index("idx_reviews_product_id", table_name="reviews")
    op.drop_index("idx_reviews_subcategory_id", table_name="reviews")
    op.drop_index("idx_reviews_category_id", table_name="reviews")
    op.drop_table("reviews")
