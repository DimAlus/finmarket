"""Implementation active model"""
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .general import Base


class Active(Base):
    """Model of active"""

    __tablename__ = "active"

    collection_id: Mapped[int] = mapped_column(__type_pos=ForeignKey("client.actives"))

    group: Mapped[int] = mapped_column(__type_pos=ForeignKey("active_group.id"))

    # percent of income for action or mass dragmet
    weight: Mapped[float]

    is_celled: Mapped[int]

    def __str__(self) -> str:
        return f"Active of {self.group} {'OPN' if self.is_celled else 'CLS'}"
