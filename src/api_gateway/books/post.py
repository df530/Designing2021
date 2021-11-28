"""
POST endpoints for adding new books' data.

Now we will post only new books with both source and meta.
But maybe in the future we will accept post something else,
connected with books. For example, post books meta before
source publication (but maybe it would be better to PUT source, not POST)
"""
from src.api_gateway.app import palt_app


@NotImplementedError
@palt_app.post("/new_book/")
def new_book(book_profile, book_src):
    """
    Add new book to books' database.

    :param book_profile: the whole information about book (except source).
    :param book_src:
    :return:
    """
    assert book_profile is not None and book_src is not None
