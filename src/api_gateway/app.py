"""
File with Fast API application
"""
from fastapi import FastAPI

palt_app = FastAPI()


@palt_app.get("/")
def start_endpoint():
    """
    Start endpoint, which will return some useful info.
    TODO
    :return:
    """
    return "Welcome to Palt!"
