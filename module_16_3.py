# -*- coding: utf-8 -*-
from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()
users = {'1': 'Имя: Example, возраст: 18'}

UserIdType = Annotated[int, Path(ge=1, le=100, description='Enter User ID', example='1')]
UsernameType = Annotated[str, Path(min_length=5, max_length=20, description='Enter username', example='UrbanUser')]
AgeType = Annotated[int, Path(ge=18, le=120, description='Enter age', example='24')]


@app.get("/users")
async def get_users() -> dict:
    return users


@app.post("/user/{username}/{age}")
async def post_user(username: UsernameType, age: AgeType) -> str:
    ind_str = str(max([int(i) for i in users.keys()]) + 1)
    users[ind_str] = f"Имя: {username}, возраст: {age}"
    return f"User {ind_str} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: UserIdType, username: UsernameType, age: AgeType):
    users[str(user_id)] = f"Имя: {username}, возраст: {age}"
    return f"User {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: UserIdType):
    users.pop(str(user_id))
    return f"User {user_id} has been deleted"
