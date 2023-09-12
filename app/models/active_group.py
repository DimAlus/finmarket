"""Model of actives prices"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .general import Base


class ActiveGroup(Base):
    """Model of actives prices"""

    __tablename__ = "active_group"

    atype: Mapped[int] = mapped_column(
        name="type",
        __type_pos=ForeignKey("active_type.id"),
    )

    # id of organisation for action or type dragmet
    owner: Mapped[int]

    # price of 1g met or 100% organisation
    price: Mapped[float]

    def __str__(self) -> str:
        return f"Group <{self.atype}> of {self.owner} ({self.price})"
