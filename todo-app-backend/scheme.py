from pydantic import BaseModel

class TasksGet(BaseModel):
    id: str
    title: str
    completed: bool

class TaskCreate(BaseModel):
    title: str


class TaskUpdata(BaseModel):
    title: str | None = None
    completed: bool | None = None


class CategorieRead(BaseModel):
    id: str
    name: str


class CategorieCreate(BaseModel):
    name: str

class CategorieUpdata(BaseModel):
    name: str

    