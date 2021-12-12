"""
PUT endpoints for adding data to existed book's id.
"""

from fastapi import Depends, UploadFile, File, HTTPException, Form

from src.api_gateway.app import palt_app, get_db
from sqlalchemy.orm import Session

from src.books.adapters import sources, info


@palt_app.put("/new_book_source/")
async def new_book_source(book_id: str = Form(...),
                          book_src: UploadFile = File(...),
                          db: Session = Depends(get_db)):
    """
    Add source of book to books' database.

    :param book_id:
    :param book_src:
    :param db: database with books' source table
    :return: book's id in database.
    """
    if info.check_book_info_with_id_exist(db, book_id) is False:
        raise HTTPException(status_code=404, detail="Not found profile of book with given id."
                                                    "Profile must be added before source")
    sources.put_source(db, book_id, book_src.file.read())
    return "Source added"
