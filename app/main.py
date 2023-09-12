"""Main file"""
from fastapi import FastAPI
from .config import get_setting

app: FastAPI

if __name__ == "app.main":
    app = FastAPI(
        docs_url=get_setting("app/docs_url", default="/docs"),
    )
    from . import routes

    print(f"Used routes from {routes.__file__}")
