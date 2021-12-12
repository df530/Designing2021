"""
Adapter to database with information about books
"""
from typing import Optional

from sqlalchemy.orm import Session

from src.api_gateway.books.schemas import BookMeta, BookProfile
from src.books.databases import models


def check_book_info_with_id_exist(db: Session, book_id: str) -> bool:
    """
    Check is information about book with given id exist in database

    :param db:
    :param book_id:
    :return:
    """
    return db.query(models.BookInfo).filter(models.BookInfo.id == book_id).first() is not None


def get_meta(db: Session, book_id: str) -> Optional[BookMeta]:
    """
    Get meta information about book from database

    :param db: database containing books' info table
    :param book_id:
    :return: None if there isn't given book id in database
    """
    book_info = db.query(models.BookInfo).filter(models.BookInfo.id == book_id).first()
    return None if book_info is None else BookMeta.from_orm(book_info)


def get_profile(db: Session, book_id: str) -> Optional[BookProfile]:
    """
    Get profile of the book from database

    :param db: database containing books' info table
    :param book_id:
    :return: None if there isn't given book id in database
    """
    book_info = db.query(models.BookInfo).filter(models.BookInfo.id == book_id).first()
    return None if book_info is None else BookProfile.from_orm(book_info)


def post_profile(db: Session, book_profile: BookProfile) -> str:
    """
    Post profile of the book to the database

    :param db: database containing books' info table
    :param book_profile:
    :return: book_id
    """
    db_book_info = models.BookInfo(**book_profile.dict())
    db.add(db_book_info)
    db.commit()
    db.refresh(db_book_info)
    return db_book_info.id
