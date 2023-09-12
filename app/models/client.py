"""Implementation client model"""
from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column, column_property

from .general import Base

# from ..lib import get_val


def get_val(obj, default):
    return default if obj is None else obj


class Client(Base):
    """Model of client"""

    __tablename__ = "client"

    # name of client
    firstname: Mapped[str] = mapped_column(String(100))
    lastname: Mapped[Optional[str]] = mapped_column(String(30))
    name = column_property(f"{firstname} {get_val(lastname, '')}".strip(" "))

    # 0 if human, 1 if organisation
    is_org: Mapped[int]
    income: Mapped[Optional[float]]

    # link to collection_id at Active
    actives: Mapped[Optional[int]]

    def __str__(self) -> str:
        return f"{'ORG' if self.is_org else 'CLT'} <{self.name}> INC {self.income}$"
