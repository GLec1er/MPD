from typing import Annotated

from pydantic import BaseModel, Field, HttpUrl
from fastapi import FastAPI, Query, Path, Body


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


# {
#     "name": "string",
#     "description": "string",
#     "price": 0,
#     "tax": 0
# }


app = FastAPI()


@app.post("/items/")
async def create_item(item: Item):
    item_dict = item.dict()
    if item.tax is not None:
        price_with_tax = item.price + item.tax
        item_dict.update({"price_with_tax": price_with_tax})
    return item_dict


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_id": item_id, **item.dict()}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item, q: str | None = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})
    return result


# Параметры функции распознаются следующим образом:
#
# Если параметр также указан в пути, он будет использоваться как параметр пути.
# Если аннотация типа параметра содержит примитивный тип ( int, float, str, bool и т.п.), он будет интерпретирован как параметр запроса .
# Если аннотация типа параметра представляет собой модель Pydantic , он будет интерпретирован как параметр тела запроса .


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None


class User(BaseModel):
    username: str
    fullname: str | None = None


@app.put("/items/{item_id}")
async def update_item(
        item_id: Annotated[int, Path(title="The ID of the item to get", ge=0, le=1000)],
        q: Annotated[str | None, Query(title='query')] = None,
        item: Item | None = None,
        user: User | None = None,
        importance: Annotated[str, Body(embed=True)] = None,

        # {
            # "item": { Вот тут появляется название поля когда embed=True
                # "name": "Foo",
                # "description": "The pretender",
                # "price": 42.0,
                # "tax": 3.2
            # }
        # }
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    if item:
        results.update({"item": item})
    if user:
        results.update({"user": user})
    return results


# ----------------------------------------------------------------------------------------------------------------------
# Field Body

class Image(BaseModel):
    url: HttpUrl | None = None
    name: str | None = None


class Item(BaseModel):
    name: str
    description: str | None = Field(
        default=None,
        title="The description of the item",
        max_length=300,
    )
    price: float = Field(
        gt=0,
        description="The price must be greater than zero",
    )
    tax: float | None = None
    tags: set[str] = set()
    image: list[Image] | None = None


class Offer(BaseModel):
    name: str
    description: str | None = None
    price: float
    items: list[Item]


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item = Body(embed=True)):
    results = {"item_id": item_id, "item": item}
    return results


# ----------------------------------------------------------------------------------------------------------------------
# Body - Вложенные модели
class Image(BaseModel):
    url: str
    name: str


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: set[str] = set()
    image: Image | None = None


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    results = {"item_id": item_id, "item": item}
    return results