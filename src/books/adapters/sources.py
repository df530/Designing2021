"""
Adapter to database with books' content
"""
from typing import Any


def get_source(book_id: str) -> Any:
    """
    Get source of the book

    :param book_id:
    :return: TODO type
    """
    raise NotImplementedError


def post_source(book_id: str, source):
    """
    Post source of the book to the database

    :param book_id:
    :param source: TODO type
    :return:
    """
    raise NotImplementedError
