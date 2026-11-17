from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import uvicorn
from uuid import uuid4

from scheme import (
    TasksGet, 
    TaskCreate, 
    TaskUpdata, 
    CategorieRead,
    CategorieCreate,
    CategorieUpdata
)


app = FastAPI()

origins = [
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


db_tasks: list[TasksGet] = []

@app.get("/tasks") 
async def get_tasks() -> list[TasksGet]:
    return db_tasks


@app.post("/tasks")
async def create_task(task:TaskCreate):
    new_task = TasksGet(id=str(uuid4()), title=task.title, completed=False)
    db_tasks.append(new_task)
    return new_task

@app.patch("/tasks/{task_id}")
async def patch_task(task_id: str, payload: TaskUpdata):
    for task in db_tasks:
        if task.id == task_id:
            if payload.title:
                task.title = payload.title 
            if payload.completed is not None:
                task.completed = payload.completed

            return task 

@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    for task in db_tasks:
        if task.id == task_id:
            db_tasks.remove(task)

db_categories: list[CategorieRead] = [] 

@app.get("/categories")
async def categories_get() -> list[CategorieRead]:
    return db_categories
    
@app.post("/categories")
async def create_categorie(paypload: CategorieCreate):
    new_categorie = CategorieRead(id=str(uuid4()), name=paypload.name)
    db_categories.append(new_categorie)
    return new_categorie

@app.patch("/categories/{id}")
async def updata_categorie(id: str, paypload: CategorieUpdata):
    for categorie in db_categories:
        if categorie.id == id:
            categorie.name = paypload.name

        return categorie

@app.delete("/categories/{id}")
async def delete_categorie(id: str):
    for categorie in db_categories:
            if categorie.id == id:
                db_categories.remove(categorie)


if "__main__" == __name__:
    uvicorn.run("main:app", host="127.0.0.1", port=8080, reload=True) 