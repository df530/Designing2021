"""
Model tables with book's information
"""
from sqlalchemy import Date, Column, Integer, String, LargeBinary

from src.books.databases import Base


class BookInfo(Base):
    __tablename__ = "books_info"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    author = Column(String)
    publication_date = Column(Date)
    description = Column(String)


class BookSource(Base):
    __tablename__ = "books_source"

    id = Column(Integer, primary_key=True)
    source = Column(LargeBinary)
