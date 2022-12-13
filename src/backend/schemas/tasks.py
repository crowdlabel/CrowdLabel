from datetime import datetime
from pydantic import BaseModel
from .questions import Question

class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    tokens: float
    questions: list[Question] # list of Question IDs


class TasksRequest(BaseModel):
    name: str | None
    reward: float | None
    requester: str | None
    page: int | None
    page_size: int | None

class TasksResponse(TasksRequest):
    tasks: list[int] # list of Task IDs
