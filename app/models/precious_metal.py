"""Model of precious metals reference"""
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .general import Base


class PreciousMetal(Base):
    """Model of precious metals reference"""

    __tablename__ = "precious_metal"

    name: Mapped[str] = mapped_column(String(5), unique=True)
    fullname: Mapped[str] = mapped_column(String(30))

    def __str__(self) -> str:
        return f"Metall type <{self.name}>"
