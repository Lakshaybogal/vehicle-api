from pydantic import BaseModel
from os import getenv
import shortid

def shorten_url(url: str):
    short_url = shortid.ShortId().generate()
    return short_url

# @app.get("/{shortURL}")
# async def redirect_to_original(shortURL: str):
#     original_url = url_database.get(shortURL)
#     if not original_url:
#         raise HTTPException(status_code=404, detail="URL not found")
#     return RedirectResponse(url=original_url)

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run(app, host="localhost", port=8000)
