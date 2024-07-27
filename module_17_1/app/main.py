# -*- coding: utf-8 -*-
from fastapi import FastAPI
from routers.user import user
from routers.task import task

app = FastAPI()


@app.get("/")
async def welcome():
    return {"message": "Welcome to Taskmanager"}


app.include_router(user)
app.include_router(task)
