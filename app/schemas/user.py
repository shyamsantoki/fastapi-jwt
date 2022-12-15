from pydantic import BaseModel


class SignupUser(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    gender: str


class DisplayUser(BaseModel):
    id: str
    username: str
    first_name: str
    last_name: str


class LoginUser(BaseModel):
    username: str
    password: str
