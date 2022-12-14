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
    introduction: Optional[str]
    description: Optional[str]
    cover:  Optional[pathlib.Path]
    tags: list[str]=[]
    responses_required: int
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    questions: list[Question]=[] # list of Questions


class TasksRequest(BaseModel):
    name: Optional[str]
    credits: Optional[float]
    requester: Optional[str]
    page: Optional[int]
    page_size: Optional[int]

class TasksResponse(TasksRequest):
    tasks: list[int] # list of Task IDs


class ErrorResponse(BaseModel):
    error: str