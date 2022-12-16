""" The schema for users endpoint """
import uuid
from enum import Enum

from pydantic import BaseModel


class UserRole(str, Enum):
    """The roles of users.

    Args:
        str (str): Datatype of fields.
        Enum (Enum): The Enum class.
    """

    user = "user"
    admin = "admin"


class SignupUser(BaseModel):
    """The data that will be asked when creating a user.

    Args:
        BaseModel (BaseModel): The base Pydantic model
    """

    username: str
    password: str
    first_name: str
    last_name: str
    email: str
    gender: str
    role: UserRole

    class Config:
        """The Pydantic configuration class."""

        use_enum_values = True


class DisplayUser(BaseModel):
    """The data that will be displayed when access token is valid.

    Args:
        BaseModel (BaseModel): The base Pydantic model.
    """

    id: uuid.UUID
    username: str
    first_name: str
    last_name: str
    role: UserRole

    class Config:
        """The Pydantic configuration class."""

        orm_mode = True
        use_enum_values = True


class LoginUser(BaseModel):
    """The data that user will enter when logging in.

    Args:
        BaseModel (BaseModel): The base Pydantic model.
    """

    username: str
    password: str
