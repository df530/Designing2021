"""
File with Fast API application
"""
from fastapi import FastAPI

from src.books.databases import BooksDatabase
from src.books.databases import models

POSTGRESQL_DATABASE_URL = None  # "postgresql://<user>:<password>@<host, 'localhost' for example>[:<port>]/books_db"
if POSTGRESQL_DATABASE_URL is None:
    raise ValueError("POSTGRESQL_DATABASE_URL is not defined")

books_db = BooksDatabase(POSTGRESQL_DATABASE_URL)

models.Base.metadata.create_all(bind=books_db.engine)
palt_app = FastAPI()


def get_db():
    db = books_db.SessionLocal()
    try:
        yield db
    finally:
        db.close()


@palt_app.get("/")
def start_endpoint():
    """
    Start endpoint, which will return some useful info.
    TODO
    :return:
    """
    return "Welcome to Palt!"
