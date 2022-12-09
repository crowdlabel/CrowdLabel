from pydantic import BaseModel



class ID(BaseModel):
    id :int 



class TaskDetails(ID):
    details:str



class Task(BaseModel):
    id: str

class TasksRequest(BaseModel):
    name: str | None
    reward: float | None
    requester: str | None
    page: int | None
    page_size: int | None

class TasksRequest(TasksRequest):
    tasks: list[Task]
    total: int

class TaskInfo(BaseModel):
    name : str
    creator : str
    details : str