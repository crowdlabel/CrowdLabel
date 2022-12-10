from datetime import datetime
from pydantic import BaseModel
from .questions import Question

class ID(BaseModel):
    id :int 



class TaskDetails(ID):
    details:str

class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    tokens: float
    questions: list[Question]


class TasksRequest(BaseModel):
    name: str | None
    reward: float | None
    requester: str | None
    page: int | None
    page_size: int | None

class TasksResponse(TasksRequest):
    tasks: list[Task]
    total: int
