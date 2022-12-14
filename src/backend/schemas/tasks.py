from datetime import datetime
from pydantic import BaseModel
from .questions import Question
from typing import Optional
import pathlib

class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    credits: float
    name: str
    introduction: str=''
    description: str=''
    cover: pathlib.Path=None
    tags: list[str]=[]
    responses_required: int
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    questions: list[Question]=[] # list of Questions

    def set_id(self, new_id):
        self.task_id = new_id


class TasksRequest(BaseModel):
    name: Optional[str]
    credits: Optional[float]
    requester: str | None
    page: int | None
    page_size: int | None

class TasksResponse(TasksRequest):
    tasks: list[int] # list of Task IDs


class ErrorResponse(BaseModel):
    error: str