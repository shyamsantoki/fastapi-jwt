from sqlalchemy import Boolean, Column, String

from app.models import Base, BaseColumns


class User(Base, BaseColumns):
    __tablename__ = "user"
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    gender = Column(String(1))
    is_active = Column(Boolean, default=False)
