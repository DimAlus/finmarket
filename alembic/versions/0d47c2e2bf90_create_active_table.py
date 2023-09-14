"""create active table

Revision ID: 0d47c2e2bf90
Revises: e2af16f1244f
Create Date: 2023-09-14 11:26:12.259290

"""
from typing import Sequence, Union

from datetime import datetime as dt
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "0d47c2e2bf90"
down_revision: Union[str, None] = "e2af16f1244f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "Construct table from Active object"
    if hasattr(op, "create_table"):
        op.create_table(
            "active",
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
                "collection_id",
                sa.Integer,
                sa.ForeignKey("client.actives"),
                nullable=False,
            ),
            sa.Column(
                "group", sa.Integer, sa.ForeignKey("active_group.id"), nullable=False
            ),
            sa.Column("weight", sa.Float, nullable=False),
            sa.Column("is_celled", sa.Integer, nullable=False),
        )


def downgrade() -> None:
    "Drop table from Active object"
    if hasattr(op, "drop_table"):
        op.drop_table("active")
