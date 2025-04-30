from typing import Annotated

from fastapi import FastAPI, Query

app = FastAPI()

fake_items_db = [
    {"item_name": "Foo"},
    {"item_name": "Bar"},
    {"item_name": "Baz"},
]


@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.get("/limit/{limit}")
async def lim(limit: int | None = None, short: bool = False):
    if short:
        return fake_items_db
    return {'limit': limit}


# ----------------------------------------------------------------------------------------------------------------------
# Расширенная валидация
@app.get("/items/")
async def read_items(
        q: Annotated[
            str | None,
            Query(
                alias='item-good', # not q there is ?item-good='1231'
                title='titletitletitle',
                description='descriptiondescriptiondescription',
                max_length=50,
                min_length=5,
                deprecated=True,
                include_in_schema=False,
            )
        ] = None
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results


# q: str | None = None == q: Annotated[str | None]