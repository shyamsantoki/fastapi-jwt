from sqlalchemy import Boolean, Column, Enum, String

from app.models import Base, BaseColumns


class User(Base, BaseColumns):
    __tablename__ = "user"
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String(1))
    role = Column(Enum("admin", "user", name="user_role", create_type=False))
    is_active = Column(Boolean, default=False)
