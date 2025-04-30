from fastapi import FastAPI, Query, Path
from typing import Annotated

# Query, Path и другие "классы", которые вы импортируете из fastapi, на самом деле являются функциями, которые
# при вызове возвращают экземпляры одноимённых классов.


app = FastAPI()


@app.get("/files/{file_path:path}") # /files/home/some/some
async def read_file(file_path: str):
    return {"file_path": file_path}


@app.get("/items/{item_id}")
async def read_items(
        item_id: Annotated[
            int,
            Path(
                title='sdfsdf',
                description='sdfgsdfg'
            )
        ],
        q: Annotated[
            str | None,
            Query(
                title='sdfsdf',
                description='dfsdfg',
                max_length=54,
                min_length=5,
                regex='',
                pattern='',
                include_in_schema=False,
            )
        ] = None
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results