"""
Adapter to database with information about books
"""

from src.books.view import BookMeta, BookProfile


@NotImplementedError
def get_meta(book_id: str) -> BookMeta:
    """
    Get meta information about book from database

    :param book_id:
    :return:
    """
    pass


@NotImplementedError
def get_profile(book_id: str) -> BookProfile:
    """
    Get profile of the book from database

    :param book_id:
    :return:
    """
    pass


@NotImplementedError
def post_profile(book_profile: BookProfile) -> str:
    """
    Post profile of the book to the database
    :return: book_id
    """
    pass
