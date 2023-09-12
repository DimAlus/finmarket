"""create client table

Revision ID: dc5eea4a29f6
Revises: 
Create Date: 2023-09-12 13:58:19.212105

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

from app.models.client import Client

# revision identifiers, used by Alembic.
revision: str = "dc5eea4a29f6"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(Client.__tablename__, *Client.__table__.columns)


def downgrade() -> None:
    op.drop_table(Client.__tablename__)
