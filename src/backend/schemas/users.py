from pydantic import BaseModel


class AvailabilityRequest(BaseModel):
    username: str | None
    email: str | None

class AvailabilityResponse(BaseModel): 
    username: bool
    email: bool




class RegistrationResponse(BaseModel):
    username: str
    email: str
    user_type: int

class RegistrationRequest(RegistrationResponse):
    password: str
    verification_code: int


class UserInfoRequest:
    username: str

