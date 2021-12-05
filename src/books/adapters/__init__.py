"""
Adapters for books' database
"""
from src.books.view import BookProfile
from src.books.adapters import info, sources


def post_book(profile: BookProfile, source) -> str:
    """
    Post profile and source of new book to the database

    :param profile:
    :param source: TODO type
    :return: book_id
    """
    book_id = info.post_profile(profile)
    sources.post_source(book_id, source)

    return book_id
