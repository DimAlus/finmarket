"""create active_type table

Revision ID: 473b24f8aa35
Revises: dc5eea4a29f6
Create Date: 2023-09-14 11:22:31.697040

"""
from typing import Sequence, Union

from datetime import datetime as dt
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "473b24f8aa35"
down_revision: Union[str, None] = "dc5eea4a29f6"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "Construct table from ActiveType object"
    if hasattr(op, "create_table"):
        op.create_table(
            "active_type",
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
            sa.Column("name", sa.String(30), unique=True, nullable=False),
        )


def downgrade() -> None:
    "Drop table from ActiveType object"
    if hasattr(op, "drop_table"):
        op.drop_table("active_type")
