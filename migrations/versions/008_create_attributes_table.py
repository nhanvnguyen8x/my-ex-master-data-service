"""create attributes table

Revision ID: 008
Revises: 007
Create Date: 2025-02-21

"""
from alembic import op
import sqlalchemy as sa

revision = "008"
down_revision = "007"
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "attributes",
        sa.Column("id", sa.String(36), nullable=False),
        sa.Column("name", sa.String(255), nullable=False),
        sa.Column("code", sa.String(100), nullable=True),
        sa.Column("status", sa.String(20), nullable=True),
        sa.Column("usage_count", sa.Integer(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_attributes_code"), "attributes", ["code"], unique=False)


def downgrade():
    op.drop_index(op.f("ix_attributes_code"), table_name="attributes")
    op.drop_table("attributes")
