"""
Endpoints for working with books
"""
from io import BytesIO
from typing import Dict, Any

from fastapi import Depends, HTTPException, Form, File, UploadFile
from fastapi.responses import StreamingResponse

from src.api_gateway.app import palt_app, get_db
from src.api_gateway.books import schemas
from src.databases.adapters.base_adapter import BaseAdapter

BOOKS_SOURCE_TABLE_NAME = "books_source"

BOOKS_INFO_TABLE_NAME = "books_info"


def get_book_info(book_id: int, db: BaseAdapter) -> Dict[str, Any]:
    info_list = db.filter_by_column_value(BOOKS_INFO_TABLE_NAME, {"id": book_id})
    if len(info_list) == 0:
        raise HTTPException(status_code=404, detail="Not found book with given id in database")
    if len(info_list) > 1:
        raise HTTPException(status_code=500, detail="Found more 1 book with this id")
    return info_list[0]


@palt_app.get("/book_meta/{book_id}", response_model=schemas.BookMeta)
async def book_meta(book_id: int, db: BaseAdapter = Depends(get_db)):
    """
    Get the book's meta from books' database

    :param book_id:
    :param db: database with books' info table
    :return:
    """
    # it would be better to do constructor of BookMeta from dict, because ORM may be not work, because some
    # field will have names, different from table in database
    return get_book_info(book_id, db)


@palt_app.get("/book_profile/{book_id}", response_model=schemas.BookProfile)
async def book_profile(book_id: int, db: BaseAdapter = Depends(get_db)):
    """
    Get the book's profile from books' database.

    :param book_id:
    :param db: database with books' info table
    :return:
    """
    return get_book_info(book_id, db)


@palt_app.get("/book_src/{book_id}")
async def book_src(book_id: int, db: BaseAdapter = Depends(get_db)):
    """
    Get the book's source from books' database.

    :param book_id:
    :param db: database with books' source table
    :return:
    """
    book_info = get_book_info(book_id, db)
    src_list = db.filter_by_column_value(BOOKS_SOURCE_TABLE_NAME, {"id": book_id})
    if len(src_list) == 0:
        raise HTTPException(status_code=404, detail="Not found book with given id in database")
    if len(src_list) > 1:
        raise HTTPException(status_code=500, detail="Found more 1 book with this id")
    response = StreamingResponse(iter(src_list[0]["source"]))
    response.headers["Content-Disposition"] = f"attachment; filename={book_info['title']}_{book_info['author']}.txt"
    return response


"""
We can't post both book's profile and source by one rout,
because (from FastAPI docs):

You can declare multiple File and Form parameters in a path operation, but you can't also
declare Body fields that you expect to receive as JSON, as the request will have the body encoded
using multipart/form-data instead of application/json.
This is not a limitation of FastAPI, it's part of the HTTP protocol.

That is why I decided to add to different endpoints: post of profile and put of book source by book's id, which
is returned after posting profile. I could make one endpoint and add fields of BookProfile as 'Form(...)', but
if BookProfile is changed (and it will be changed one day) we will have to change this endpoint too.
"""


@palt_app.post("/new_book_profile/")
async def new_book_profile(book_profile: schemas.BookProfile,
                           db: BaseAdapter = Depends(get_db)):
    """
    Add new book profile to books' database.

    :param book_profile: the whole information about book (except source).
    :param db: database with books' profiles table
    :return: book's id in database.
    """
    book_id = db.get_table_size(BOOKS_INFO_TABLE_NAME) + 1
    db.add_elem_to_table(BOOKS_INFO_TABLE_NAME, {**book_profile.dict()})
    return {"book_id": book_id}


@palt_app.post("/new_book_source/")
async def new_book_source(book_id: int = Form(...),
                          book_src: UploadFile = File(...),
                          db: BaseAdapter = Depends(get_db)):
    """
    Add source of book to books' database.

    :param book_id:
    :param book_src:
    :param db: database with books' source table
    :return: book's id in database.
    """
    if len(db.filter_by_column_value(BOOKS_INFO_TABLE_NAME, {"id": book_id})) == 0:
        raise HTTPException(status_code=404, detail="Not found profile of book with given id."
                                                    "Profile must be added before source")
    db.add_elem_to_table(BOOKS_SOURCE_TABLE_NAME, {"id": book_id}, {"source": BytesIO(book_src.file.read())})
    return "Source added"
