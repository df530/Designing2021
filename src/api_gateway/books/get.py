"""
GET endpoints for getting different books' data
"""
from src.api_gateway.app import palt_app


@NotImplementedError
@palt_app.get("/book_meta/{book_id}")
def book_meta(book_id: str):
    """
    Get the book's meta from books' database.

    :param book_id:
    :return:
    """
    assert book_id != ""


@NotImplementedError
@palt_app.get("/book_profile/{book_id}")
def book_profile(book_id: str):
    """
    Get the book's profile from books' database.

    :param book_id:
    :return:
    """
    assert book_id != ""


@NotImplementedError
@palt_app.get("/book_src/{book_id}")
def book_src(book_id: str):
    """
    Get the book's source from books' database.

    :param book_id:
    :return:
    """
    assert book_id != ""
