"""
Adapter to database with books' content
"""
from io import BytesIO
from typing import Optional

from sqlalchemy.orm import Session

from src.books.databases import models


def get_source(db: Session, book_id: str) -> Optional[BytesIO]:
    """
    Get source of the book

    :param db: database containing books' source table
    :param book_id:
    :return: stream with source bytes. Return None if source wasn't found
    """
    src: Optional[models.BookSource] = db.query(models.BookSource).filter(models.BookSource.id == book_id).first()
    return None if src is None else BytesIO(src.source)


def put_source(db: Session, book_id: str, source: bytes):
    """
    Post source of the book to the database

    :param db: database containing books' source table
    :param book_id:
    :param source:
    :return:
    """
    db_book_src = models.BookSource(id=book_id, source=source)
    db.add(db_book_src)
    db.commit()
    db.refresh(db_book_src)
