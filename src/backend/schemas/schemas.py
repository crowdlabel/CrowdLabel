from pydantic import BaseModel


class ID(BaseModel):
    id :int 

class Email(BaseModel):
    email: str

class TaskDetails(ID):
    details:str

class Credentials(BaseModel):
    username: str
    password: str

class Registration(Email, Credentials):
    user_type: int
    verification_code: str

class Task(BaseModel):
    id: str

class TasksRequest(BaseModel):
    name: str | None
    reward: float | None
    requester: str | None
    page: int | None
    page_size: int | None

class TasksRequest(TasksRequest):
    tasks: list[Task]
    total: int

class TaskInfo(BaseModel):
    name : str
    creator : str
    details : str
class QuestionInfo(BaseModel):
    type: str
    prompt :str
    resource:str
    options:str
    task_id :int
class IDWithQuestionInfo(QuestionInfo):
    id :int

class UserInfoRequest:
    username: str

class AuthenticatedRequest:
    jwt: str


class ResultInfo(BaseModel):
    task_name:str
    task_ID:int


class Availability(BaseModel):
    username: str | None
    email: str | None

