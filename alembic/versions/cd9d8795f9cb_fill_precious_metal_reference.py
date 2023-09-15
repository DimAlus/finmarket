"""fill precious_metal reference

Revision ID: cd9d8795f9cb
Revises: 0d47c2e2bf90
Create Date: 2023-09-14 13:44:41.752515

"""
from typing import Sequence, Union

import sqlalchemy as sa
from sqlalchemy.sql import table, column as col
from alembic import op


# revision identifiers, used by Alembic.
revision: str = "cd9d8795f9cb"
down_revision: Union[str, None] = "0d47c2e2bf90"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    "fill precious_metal reference"
    # if hasattr(op, "bulk_insert"):
    #     op.bulk_insert(
    #         table(
    #             "precious_metal",
    #             col("name", sa.String),
    #             col("fullname", sa.String),
    #         ),
    #         [
    #             {"name": "XAU", "fullname": "Золото"},
    #             {"name": "XAG", "fullname": "Серебро"},
    #             {"name": "XPT", "fullname": "Платина"},
    #             {"name": "XPD", "fullname": "Палладий"},
    #         ],
    #     )
    if hasattr(op, "execute"):
        op.execute(
            """
                   INSERT INTO precious_metal 
                   (name, fullname) 
                   VALUES 
                   ('XAU', 'Золото'),
                   ('XAG', 'Серебро'),
                   ('XPT', 'Платина'),
                   ('XPD', 'Палладий');
                   """
        )


def downgrade() -> None:
    "delete from precious_metal reference"
    if hasattr(op, "execute"):
        op.execute("DELETE FROM precious_metal;")
