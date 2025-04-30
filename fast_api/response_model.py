from fastapi import FastAPI, Response, Path
from fastapi.responses import JSONResponse, RedirectResponse
from pydantic import BaseModel, EmailStr
from typing import Annotated

app = FastAPI()


class ItemRq(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None
    tags: list[str] = []


class ItemRs(BaseModel):
    name: str
    price: float

# Вы можете объявить тип ответа, указав аннотацию возвращаемого значения для функции операции пути .
@app.post("/items/")
async def create_item(item: ItemRs) -> ItemRs:
    return item


@app.get("/items/")
async def read_items() -> list[ItemRs]:
    return [
        ItemRs(name="Portal Gun", price=42.0),
        ItemRs(name="Plumbus", price=32.0),
    ]


# Параметр response_model может быть указан для любой операции пути :
@app.post("/items/", response_model=ItemRs)
async def create_item(item: ItemRs) -> ItemRs:
    return item


# Возвращаемый тип и Фильтрация данных
class BaseUser(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(BaseUser):
    password: str


@app.post("/user/", response_model=BaseUser)
async def create_user(user: UserIn) -> BaseUser:
    return user


# Возвращаем Response
@app.get("/portal")
async def get_portal(teleport: bool = False) -> Response:
    if teleport:
        return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")
    return JSONResponse(content={"message": "Here's your interdimensional portal."})


@app.get("/portal", response_model=None)
async def get_portal(teleport: bool = False) -> Response | dict:
    return RedirectResponse(url="https://www.youtube.com/watch?v=dQw4w9WgXcQ")


# Параметры модели ответа
class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float = 10.5
    tags: list[str] = []


items = {
    "foo": {"name": "Foo", "price": 50.2},
    "bar": {"name": "Bar", "description": "The bartenders", "price": 62, "tax": 20.2},
    "baz": {"name": "Baz", "description": None, "price": 50.2, "tax": 10.5, "tags": []},
}


@app.get(
    "/items/{item_id}",
    response_model=Item,
    response_model_exclude_unset=True,
    response_model_exclude={'name', },
    response_model_include=set('price',)
)
        # response_model_exclude_unset если пустое поле то его не добавляем в ответ
        # {
        #     "name": "Foo",
        #     "price": 50.2
        # }
async def read_item(item_id: Annotated[str, Path()]) -> Item:
    return items[item_id]


# ----------------------------------------------------------------------------------------------------------------------
# Дополнительные модели
class UserBase(BaseModel):
    username: str
    email: EmailStr
    full_name: str | None = None


class UserIn(UserBase):
    password: str


class UserOut(UserBase):
    pass


class UserInDB(BaseUser):
    hashed_password: str


def fake_password_hasher(raw_password: str):
    return "supersecret" + raw_password


def fake_save_user(user_in: UserIn):
    hashed_password = fake_password_hasher(user_in.password)
    user_in_db = UserInDB(**user_in.dict(), hashed_password=hashed_password)

    # UserInDB(
    #     username = user_dict["username"],
    #     password = user_dict["password"],
    #     email = user_dict["email"],
    #     full_name = user_dict["full_name"],
    #     hashed_password = hashed_password,
    # )

    print("User saved! ..not really")
    return user_in_db


@app.post("/user/", response_model=UserOut)
async def create_user(user_in: UserIn):
    user_saved = fake_save_user(user_in)
    return user_saved


