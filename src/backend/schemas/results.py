from pydantic import BaseModel

class ResultInfo(BaseModel):
    task_name:str
    task_ID:int