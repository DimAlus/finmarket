"""General objects and params for all models"""
from sqlalchemy.orm import DeclarativeBase
import sqlalchemy as __sqlalch
from ..config import get_setting as __get_setting

engine: __sqlalch.Engine


class Base(DeclarativeBase):
    """Base"""


def __create_engine() -> __sqlalch.Engine:
    """Set engine variable"""

    dialect = __get_setting("database/dialect", default="sqlite")
    driver = __get_setting("database/driver", default="pysqlite")
    user = __get_setting("database/user", default="")
    passwd = __get_setting("database/pass", default="")
    host = __get_setting("database/host", default="")
    dbname = __get_setting("database/dbname", default="db.db")

    if driver != "":
        driver = f"+{driver}"
    if user != "":
        passwd = f":{passwd}"

    return __sqlalch.create_engine(
        f"{dialect}{driver}://{user}{passwd}@{host}/{dbname}"
    )


engine = __create_engine()
