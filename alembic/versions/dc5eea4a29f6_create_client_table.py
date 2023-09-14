"""create client table

Revision ID: dc5eea4a29f6
Revises: 
Create Date: 2023-09-12 13:58:19.212105

"""
from typing import Sequence, Union

from datetime import datetime as dt
import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "dc5eea4a29f6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "Construct table from Client object"
    if hasattr(op, "create_table"):
        op.create_table(
            "client",
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
            sa.Column("firstname", sa.String(100), nullable=False),
            sa.Column("lastname", sa.String(30)),
            sa.Column("is_org", sa.Integer, nullable=False),
            sa.Column("income", sa.Float),
            sa.Column("actives", sa.Integer),
        )


def downgrade() -> None:
    "Drop table from Client object"
    if hasattr(op, "drop_table"):
        op.drop_table("client")
