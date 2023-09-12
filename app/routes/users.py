"""Routes for users"""
from typing import Optional
import json
from fastapi import Request, Body, Response
from sqlalchemy import text
from ..main import app

from ..models import engine, Client


@app.get("/client")
def get_clients():
    """index"""

    # with engine.connect() as conn:
    #     res = conn.execute(text("SELECT id FROM client"))

    return {"message": "ss"}


def create_client(name: str, sername: str | None, is_org: bool, income: float | None):
    """Creating client into db"""
    Client(firstname=name, lastname=sername, is_org=int(is_org), income=income)


@app.post("/client/add")
async def add_client(
    name: str = Body(),
    sername: Optional[str] = Body(default=None),
    income: Optional[float] = Body(default=None),
):
    """Add new client to database"""

    print(name, sername, income)
    create_client(name=name, sername=sername, is_org=False, income=income)
    return Response(json.dumps({"message": "User added"}))
