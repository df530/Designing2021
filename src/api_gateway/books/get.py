"""
GET endpoints for getting different books' data
"""
import datetime
from typing import Any

from src.api_gateway.app import palt_app
from src.books.view import BookMeta, BookProfile
from src.books.adapters import info, sources


@palt_app.get("/book_meta/{book_id}")
async def book_meta(book_id: str) -> BookMeta:
    """
    Get the book's meta from books' database.

    :param book_id:
    :return:
    """
    return info.get_meta(book_id)


@palt_app.get("/book_profile/{book_id}")
def book_profile(book_id: str) -> BookProfile:
    """
    Get the book's profile from books' database.

    :param book_id:
    :return:
    """
    return info.get_profile(book_id)


@palt_app.get("/book_src/{book_id}")
def book_src(book_id: str) -> Any:
    """
    Get the book's source from books' database.

    :param book_id:
    :return:
    """
    return sources.get_source(book_id)
