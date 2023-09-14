"""General objects and params for all models"""
from datetime import datetime
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
import sqlalchemy
from ..config import get_setting as __get_setting

engine: sqlalchemy.Engine


class Base(DeclarativeBase):
    """Base"""

    id: Mapped[int] = mapped_column(primary_key=True, unique=True, autoincrement=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now())
    updated_at: Mapped[datetime] = mapped_column(
        default=datetime.now,
        onupdate=datetime.now,
    )


def __create_engine() -> sqlalchemy.Engine:
    """Set engine variable"""

    dialect = __get_setting("database/dialect", default="sqlite")
    driver = __get_setting("database/driver", default="pysqlite")
    user = __get_setting("database/user", default="")
    passwd = __get_setting("database/pass", default="")
    hostname = __get_setting("database/host", default="")
    dbname = __get_setting("database/dbname", default="db.db")

    if driver != "":
        driver = f"+{driver}"
    if user != "":
        passwd = f":{passwd}"
    if hostname != "":
        hostname = f"@{hostname}"

    host = f"{dialect}{driver}://{user}{passwd}{hostname}/{dbname}"
    # print(f"Connection to {host}")
    return sqlalchemy.create_engine(host)


engine = __create_engine()
