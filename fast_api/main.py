# Команда uvicorn main:app обращается к:
#
# main: файл main.py (модуль Python).
# app: объект, созданный внутри файла main.py в строке app = FastAPI().
# --reload: перезапускает сервер после изменения кода. Используйте только для разработки.

# uvicorn main:app --reload
# ----------------------------------------------------------------------------------------------------------------------


from fastapi import FastAPI

app = FastAPI(title='Simple FastAPI',) # экземпляр FastAPI


@app.get('/items/me')
async def me() -> dict:
    return {'item_id': 'me'}


@app.get('/items/{item_id}')
async def root(item_id: int) -> dict:
    return {'item_id': item_id}
