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


class Task(BaseModel):
    task_id: int
    creator: str
    date_created: datetime
    credits: float
    name: str
    introduction: str=''
    description: str=''
    cover: str=''
    tags: list[str]=[]
    responses_required: int
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    questions: list[schemas.questions.Question]=[] # list of Questions
    def __init__(self,task):
        super(Task,self).__init__(task_id = task.id,creator = task.creator ,date_created = task.date_created,
        credits = task.credits , name = task.name , introduction = task.introduction ,
        description = task.description ,cover = task.cover_path,responses_required = task.response_required,
        tags =[task.tags])
