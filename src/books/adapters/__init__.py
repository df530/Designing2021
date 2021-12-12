"""
Adapters for books' database
"""
from typing import Optional

from sqlalchemy.orm import Session

from src.api_gateway.books.schemas import BookProfile
from src.books.adapters import info, sources


def post_book(db_book_info: Session, profile: BookProfile, source: bytes,
              db_book_src: Optional[Session] = None) -> str:
    """
    Post profile and source of new book to the database

    :param db_book_info: database containing books' info table
    :param profile:
    :param source:
    :param db_book_src: database containing books' source table.
                        If None, it like books' info database
    :return: book_id
    """
    if db_book_src is None:
        db_book_src = db_book_info
    book_id = info.post_profile(db_book_info, profile)
    sources.put_source(db_book_src, book_id, source)

    return book_id
