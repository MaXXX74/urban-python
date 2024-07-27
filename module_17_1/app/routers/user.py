# -*- coding: utf-8 -*-
from fastapi import APIRouter

user = APIRouter(prefix="/user", tags=["user"])


@user.get("/")
async def all_users():
    pass


@user.get("/user_id")
async def user_by_id():
    pass


@user.post("/create")
async def create_user():
    pass


@user.put("/update")
async def update_user():
    pass


@user.delete("/delete")
async def delete_user():
    pass
