"""
GET endpoints for getting different books' data
"""
from io import BytesIO
from typing import Optional

from fastapi import Depends, HTTPException
from fastapi.responses import StreamingResponse, FileResponse, Response
from sqlalchemy.orm import Session

from src.api_gateway.app import palt_app, get_db
from src.api_gateway.books import schemas
from src.books.adapters import info, sources


@palt_app.get("/book_meta/{book_id}", response_model=schemas.BookMeta)
async def book_meta(book_id: str, db: Session = Depends(get_db)):
    """
    Get the book's meta from books' database

    :param book_id:
    :param db: database with books' info table
    :return:
    """
    meta = info.get_meta(db, book_id)
    if meta is None:
        raise HTTPException(status_code=404, detail="Not found book with given id in database")
    return meta


@palt_app.get("/book_profile/{book_id}", response_model=schemas.BookProfile)
async def book_profile(book_id: str, db: Session = Depends(get_db)):
    """
    Get the book's profile from books' database.

    :param book_id:
    :param db: database with books' info table
    :return:
    """
    profile = info.get_profile(db, book_id)
    if profile is None:
        raise HTTPException(status_code=404, detail="Not found book with given id in database")
    return profile


@palt_app.get("/book_src/{book_id}")
async def book_src(book_id: str, db: Session = Depends(get_db)):
    """
    Get the book's source from books' database.

    :param book_id:
    :param db: database with books' source table
    :return:
    """
    meta = info.get_meta(db, book_id)
    if meta is None:
        raise HTTPException(status_code=404, detail="Not found book with given id in database")
    src: Optional[BytesIO] = sources.get_source(db, book_id)
    if src is None:
        raise HTTPException(status_code=404, detail="Not found source of book with given id")
    response = StreamingResponse(iter([src.getvalue()]))
    response.headers["Content-Disposition"] = f"attachment; filename={meta.title}_{meta.author}.txt"
    return response
