from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import schemas.questions


class TaskSearchRequest(BaseModel):
    name: Optional[str]
    tags: Optional[set[str]]
    requesters: Optional[set[str]]
    page: Optional[int]
    credits_min: Optional[float]
    credits_max: Optional[float]
    sort_criteria: Optional[str]
    sort_ascending: Optional[bool]

class TaskSearchResponse(TaskSearchRequest):
    tasks: list[int]=[] # list of Task IDs
    total: int=0 # total number of tasks

class ErrorResponse(BaseModel):
    error: str


class CreateTaskRequest(BaseModel):
    name: str
    credits: float
    introduction: str=''
    description: str=''
    tags: list[str]=[]
    responses_required: int
    questions: list[schemas.questions.Question]=[] # list of Questions

class Task(CreateTaskRequest):
    task_id: int
    creator: str
    cover: str=''
    date_created: datetime
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task