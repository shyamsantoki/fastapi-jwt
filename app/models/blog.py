from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Text
from sqlalchemy.dialects.postgresql import UUID

from app.models import Base, BaseColumns


class Blog(Base, BaseColumns):
    __tablename__ = "blog"
    author = Column(UUID(as_uuid=True), ForeignKey("user.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    status = Column(Enum("published", "draft", name="blog_status", create_type=False))
    date = Column(DateTime, default=datetime.utcnow)
