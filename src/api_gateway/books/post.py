"""
POST endpoints for adding new books' data.
"""
from fastapi import Depends

from src.api_gateway.app import palt_app, get_db
from sqlalchemy.orm import Session
from src.api_gateway.books.schemas import BookProfile
from src.books.adapters import info

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
async def new_book_profile(book_profile: BookProfile,
                           db: Session = Depends(get_db)):
    """
    Add new book profile to books' database.

    :param book_profile: the whole information about book (except source).
    :param db: database with books' profiles table
    :return: book's id in database.
    """
    book_id = info.post_profile(db, book_profile)
    return {"book_id": book_id}
