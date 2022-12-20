from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
import schemas.questions
import re

class TaskSearchRequest(BaseModel):
    """
The following are all valid search parameters:\n
`name`: name of the task, empty name searches for any task\n
`tags`: keywords that identify the type of task, for example "object-detection"\n
`requesters`: username of the requesters who created task, empty searches for any requester\n
`credits_min`, `credits_max`: minimum and maximum number of credits rewarded upon task completion; negative `credits_max` implies no upper limit\n
`questions_min`, `questions_max`: minimum and maximum number of questions in the task; negative `questions_max` implies no upper limit\n
`page`: the page; negative value counts backwards, e.g. -1 returns the last page\n
`page_size`: the size of each page; if -1 then `page` would not be considered and all results will be returned, e.g.:\n
- if `page` is 2 and `page_size` is 10, then it will return the 11th to 20th results, inclusive\n
- if `page` is _ and `page_size` is -1, then it will return all the results\n
- if `page` is -1, `page_size` is 10, and there are 26 results in total, then it will return the 21st to 26th results, inclusive\n
`sort_criteria`: search parameter that the results should be sorted against\n
`sort_ascending`: True to sort in ascending order, False to sort in descending order
    """
    
    name: Optional[str] = ''
    tags: Optional[set[str]] = set()
    requesters: Optional[set[str]] = set()
    page: Optional[int] = 1 
    page_size: Optional[int] = -1
    credits_min: Optional[float] = 0
    credits_max: Optional[float] = -1
    questions_min: Optional[int] = 0
    questions_max: Optional[int] = -1
    sort_criteria: Optional[str] = 'name'
    sort_ascending: Optional[bool] = True

class TaskSearchResponse(BaseModel):
    tasks: list[int]=[] # list of Task IDs
    total: int=0 # total number of tasks

class ErrorResponse(BaseModel):
    error: str


class Tag(BaseModel):
    tag: str

    __chars = 'a-z0-9\+#\-\.' # https://stackoverflow.help/en/articles/5611219-create-a-tag
    __pattern = re.compile(f'[{__chars}]+')
    @validator('tag')
    def tag_format(cls, tag):
        tag = tag.replace(' ', '-')
        tag = tag.lower()
        if not re.fullmatch(cls.__pattern, tag):
            raise ValueError('Invalid tag')
        return tag

        

class CreateTaskRequest(BaseModel):
    name: str='My Task'
    credits: float=0
    introduction: str=''
    description: str=''
    cover_image: str=''
    tags: set[str]=set()
    responses_required: int=1
    questions: list[schemas.questions.Question]=[] # list of Questions

class Task(CreateTaskRequest):
    task_id: int
    requester: str
    date_created: datetime
    respondents_claimed: set[str]=set() # usernames of respondents who have claimed the task but have not completed it
    respondents_completed: set[str]=set() # usernames of respondents who have claimed and completed the task
    """ def __init__(self,task):
        super(Task,self).__init__(task_id = task.id,creator = task.creator ,date_created = task.date_created,
        credits = task.credits , name = task.name , introduction = task.introduction ,
        description = task.description ,cover = task.cover_path,responses_required = task.response_required,
        tags =[task.tags]) """
