from pydantic import BaseModel
from os import getenv
import shortid

def shorten_url(url: str):
    short_url = shortid.ShortId().generate()
    return short_url
