"""Implementation active model"""
from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .general import Base


class Active(Base):
    """Model of active"""

    __tablename__ = "active"

    id: Mapped[int] = mapped_column(primary_key=True)
    collection_id: Mapped[int] = mapped_column(__type_pos=ForeignKey("client.actives"))

    atype: Mapped[int] = mapped_column(
        name="type",
        __type_pos=ForeignKey("active_type.id"),
    )

    # id of organisation for action or type dragmet
    owner: Mapped[int]

    # percent of income for action or mass dragmet
    weight: Mapped[float]

    is_celled: Mapped[int]


class ActiveType(Base):
    """Model of active type reference"""

    __tablename__ = "active_type"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))


class PreciousMetal(Base):
    """Model of precious metals reference"""

    __tablename__ = "precious_metal"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    price: Mapped[float]
