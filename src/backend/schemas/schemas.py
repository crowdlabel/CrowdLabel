from pydantic import BaseModel



class ID(BaseModel):
    id :int 

class Email(BaseModel):
    email: str

class TaskDetails(ID):
    details:str
    introduction:str

class ChildTaskResponse(ID):
    response:str

class Credentials(BaseModel):
    username: str
    password: str

class Registration(Email, Credentials):
    user_type: int
    verification_code: str

class TaskInfo(BaseModel):
    name : str
    creator : str
    details: str
    introduction : str
    type : int 
    path : str

class FilePath(ID):
    path:str
class QuestionInfo(BaseModel):
    type: str
    prompt :str
    resource:str
    options:str
    task_id :int
class IDWithQuestionInfo(QuestionInfo):
    id :int
class AuthenticatedRequest(BaseModel):
    jwt: str

class UserInfoRequest(AuthenticatedRequest):
    username: str

class JWT(BaseModel):
    jwt: str

class AuthenticatedRequest(BaseModel):
    jwt: str

class Task(AuthenticatedRequest):
    id: str
class ResultInfo(BaseModel):
    task_name:str
    task_ID:int
class ChildResultInfo(BaseModel):
    response:str
    result_id:int 
