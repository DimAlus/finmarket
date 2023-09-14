"""create precious_metal table

Revision ID: 2f2ddbda9a55
Revises: 473b24f8aa35
Create Date: 2023-09-14 11:24:19.358202

"""
from typing import Sequence, Union

from datetime import datetime as dt
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "2f2ddbda9a55"
down_revision: Union[str, None] = "473b24f8aa35"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "Construct table from PreciousMetal object"
    if hasattr(op, "create_table"):
        op.create_table(
            "precious_metal",
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
            sa.Column("name", sa.String(5), unique=True, nullable=False),
            sa.Column("fullname", sa.String(30), nullable=False),
        )


def downgrade() -> None:
    "Drop table from PreciousMetal object"
    if hasattr(op, "drop_table"):
        op.drop_table("precious_metal")
