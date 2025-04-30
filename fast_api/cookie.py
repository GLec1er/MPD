from fastapi import FastAPI, Cookie, Query
from typing import Annotated

from pydantic import BaseModel

app = FastAPI()


@app.get("/items/")
async def read_items(ads_id: str | None = Cookie(default=None)):
    return {"ads_id": ads_id}


@app.get("/items/")
async def read_items(ads_id: Annotated[str | None, Cookie(default=None)]):
    return {"ads_id": ads_id}


class Cookies(BaseModel):
    model_config = {"extra": "forbid"}

    session_id: str
    fatebook_tracker: str | None = None
    google_tracker: str | None = None


@app.get("/cookies/")
async def read_cookies(cookies: Annotated[Cookies, Cookie()]):
    return {"cookies": cookies}