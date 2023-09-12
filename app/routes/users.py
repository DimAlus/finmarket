"""Routes for users"""

from ..main import app


@app.get("/")
def root():
    """index"""
    return {"message": "OK"}


@app.get("/a")
def roota():
    """index"""
    return {"message": "OKEY"}
