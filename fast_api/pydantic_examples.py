from fastapi import FastAPI, Body
from pydantic import BaseModel, Field
from typing import Annotated

app = FastAPI()


class Item(BaseModel):
    name: str
    description: str | None = Field(default=None, examples=['sdfgdsfgd'])
    price: float
    tax: float | None = None

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                }
            ]
        }
    }


@app.put("/items/{item_id}")
# Параметр Body с аргументом example
async def update_item(
        item_id: int,
        item: Annotated[Item, Body(
            examples=[
                {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
                {
                    "name": "Bar",
                    "price": "35.4",
                },
                {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            ]
        )],
):
    results = {"item_id": item_id, "item": item}
    return results
