"""Model of active type reference"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .general import Base


class ActiveType(Base):
    """Model of active type reference"""

    __tablename__ = "active_type"

    name: Mapped[str] = mapped_column(String(30))

    def __str__(self) -> str:
        return f"T<{self.name}>"
