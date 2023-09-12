"""Implementation client model"""
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, column_property

from .general import Base
from ..lib import get_val


class Client(Base):
    """Model of client"""

    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)

    # name of client
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[Optional[str]] = mapped_column(String(30))
    name = column_property(f"{firstname} {get_val(lastname, '')}".strip(" "))

    # 0 if human, 1 if organisation
    is_org: Mapped[int]
    income: Mapped[Optional[float]]

    # link to collection_id at Active
    actives: Mapped[Optional[int]]
