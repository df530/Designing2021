"""
File with Fast API application
"""
from fastapi import FastAPI

from src.databases.adapters import PostgresqlAdapter, BaseAdapter

palt_app = FastAPI()


def get_db():
    db: BaseAdapter = None  # PostgresqlAdapter(<hostname>, <port>, <username>, <password>, <database>)
    if db is None:
        raise ValueError("Database is not set")
    yield db


@palt_app.get("/")
def start_endpoint():
    """
    Start endpoint, which will return some useful info.
    TODO
    :return:
    """
    return "Welcome to Palt!"
