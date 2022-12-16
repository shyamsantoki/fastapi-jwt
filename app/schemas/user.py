import uuid

from pydantic import BaseModel


class SignupUser(BaseModel):
    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    gender: str
    role: str


class DisplayUser(BaseModel):
    id: uuid.UUID
    username: str
    first_name: str
    last_name: str

    class Config:
        orm_mode = True


class LoginUser(BaseModel):
    username: str
    password: str
