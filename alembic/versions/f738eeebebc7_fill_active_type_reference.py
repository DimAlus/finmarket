"""fill active_type reference

Revision ID: f738eeebebc7
Revises: cd9d8795f9cb
Create Date: 2023-09-14 13:44:59.541533

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.sql import table, column as col
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "f738eeebebc7"
down_revision: Union[str, None] = "cd9d8795f9cb"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "fill active_type reference"
    if hasattr(op, "bulk_insert"):
        op.bulk_insert(
            table(
                "active_type",
                col("name", sa.String),
            ),
            [
                {"name": "SHARE"},
                {"name": "PRECMET"},
            ],
        )


def downgrade() -> None:
    "delete from active_type reference"
    if hasattr(op, "execute"):
        op.execute("DELETE FROM active_type;")
