"""
Model of book's information, that is stored in books' info database
"""
from datetime import date


class BookInfo:
    """Model of row in books' information database"""
    def __init__(self, identifier: str, title: str, author: str, publication_date: date,
                 description: str):
        self.identifier = identifier
        self.title = title
        self.author = author
        self.publication_date = publication_date
        self.description = description
