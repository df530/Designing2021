"""
Classes for viewing information about books
"""

from src.books.databases.models.info import BookInfo


class BookMeta:
    """Data, which contains main information about book"""
    def __init__(self, book_info: BookInfo):
        self.title = book_info.title
        self.author = book_info.title


class BookProfile:
    """Data, which contains whole information about book (except for content)"""
    def __init__(self, book_info: BookInfo):
        self.title = book_info.title
        self.author = book_info.author
        self.publication_date = book_info.publication_date
        self.description = book_info.description


class BookSource:
    """Source of the book"""

