from pydantic import BaseModel



class QuestionInfo(BaseModel):
    type: str
    prompt :str
    resource:str
    options:str
    task_id :int

class IDWithQuestionInfo(QuestionInfo):
    id :int








