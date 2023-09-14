"""create active_group table

Revision ID: e2af16f1244f
Revises: 2f2ddbda9a55
Create Date: 2023-09-14 11:25:15.793430

"""
from typing import Sequence, Union

from datetime import datetime as dt
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "e2af16f1244f"
down_revision: Union[str, None] = "2f2ddbda9a55"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "Construct table from ActiveGroup object"
    if hasattr(op, "create_table"):
        op.create_table(
            "active_group",
            sa.Column(
                "id",
                sa.Integer,
                unique=True,
                primary_key=True,
                autoincrement=True,
                nullable=False,
            ),
            sa.Column("created_at", sa.DateTime, nullable=False, default=dt.now),
            sa.Column(
                "updated_at",
                sa.DateTime,
                nullable=False,
                default=dt.now,
                onupdate=dt.now,
            ),
            sa.Column(
                "type", sa.Integer, sa.ForeignKey("active_type.id"), nullable=False
            ),
            sa.Column("owner", sa.Integer, nullable=False),
            sa.Column("price", sa.Float, nullable=False),
        )


def downgrade() -> None:
    "Drop table from ActiveGroup object"
    if hasattr(op, "drop_table"):
        op.drop_table("active_group")
