from pydantic import BaseModel


class AvailabilityRequest(BaseModel):
    username: str | None
    email: str | None

class AvailabilityResponse(BaseModel): 
    username: bool
    email: bool






class Email(BaseModel):
    email: str


class Credentials(BaseModel):
    username: str
    password: str


class Registration(Email, Credentials):
    user_type: int
    verification_code: str

class UserInfoRequest:
    username: str

