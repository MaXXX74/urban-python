# -*- coding: utf-8 -*-
from fastapi import APIRouter

task = APIRouter(prefix="/task", tags=["task"])


@task.get("/")
async def all_tasks():
    pass


@task.get("/task_id")
async def task_by_id():
    pass


@task.post("/create")
async def create_task():
    pass


@task.put("/update")
async def update_task():
    pass


@task.delete("/delete")
async def delete_task():
    pass
