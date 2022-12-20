from pydantic import BaseModel
from typing import Optional
from datetime import datetime
import schemas.questions


class TaskSearchRequest(BaseModel):
    name: Optional[str] = '' # empty name searches for any name
    tags: Optional[set[str]] = set()
    requesters: Optional[set[str]] = set()
    page: Optional[int] = 1
    page_size: Optional[int] = -1 # negative value implies return all results
    credits_min: Optional[float] = 0
    credits_max: Optional[float] = -1 # negative value implies no upper limit
    sort_criteria: Optional[str] = 'name'
    sort_ascending: Optional[bool] = True

class TaskSearchResponse(TaskSearchRequest):
    tasks: list[int]=[] # list of Task IDs
    total: int=0 # total number of tasks

class ErrorResponse(BaseModel):
    error: str


class CreateTaskRequest(BaseModel):
    name: str='My Task'
    credits: float=0
    introduction: str=''
    description: str=''
    tags: set[str]=set()
    responses_required: int=1
    questions: list[schemas.questions.Question]=[] # list of Questions

class Task(CreateTaskRequest):
    task_id: int
    creator: str
    cover: str=''
    date_created: datetime
    questions: list[schemas.questions.Question]=[] # list of Questions
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    def __init__(self,task):
        super(Task,self).__init__(task_id = task.id,creator = task.creator ,date_created = task.date_created,
        credits = task.credits , name = task.name , introduction = task.introduction ,
        description = task.description ,cover = task.cover_path,responses_required = task.response_required,
        tags =[task.tags])
