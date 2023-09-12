"""This module read toml files and create configuraton objects"""
from typing import Any
from os.path import dirname, join as pathjoin, exists as fexists
from toml import load as tomload

current_path: str = dirname(__file__)
current_file: str = (
    "settings.overload.py" if fexists("settings.overload.py") else "settings.toml"
)

settings: dict[str, Any] = tomload(pathjoin(current_path, current_file))


def get_setting(path: str, *, default: Any = "", sep="/"):
    """Get object of settings"""
    obj = settings
    for elem in path.split(sep=sep):
        if isinstance(obj, dict) and elem in obj:
            obj = obj[elem]
        else:
            return default
    return obj
