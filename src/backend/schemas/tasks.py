from pydantic import BaseModel
from typing import Optional




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