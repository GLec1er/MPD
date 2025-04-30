from typing import Annotated

from fastapi import FastAPI, Header
from pydantic import BaseModel

app = FastAPI()


@app.get("/items/")
async def read_items(user_agent: Annotated[str | None, Header(convert_underscores=False)] = None):
    return {"User-Agent": user_agent}


@app.get("/items/")
async def read_items(user_agent: Annotated[list[str] | None, Header(convert_underscores=False)] = None):
    return {"User-Agent": user_agent}


class CommonHeaders(BaseModel):
    model_config = {
        "extra": "forbid"
    }

    host: str
    save_data: bool
    if_modified_since: str | None = None
    traceparent: str | None = None
    x_tag: list[str] = []


@app.get("/items/")
async def read_items(
        headers: Annotated[
            CommonHeaders,
            Header(
                convert_underscores=False
            )
        ]
):
    return headers
