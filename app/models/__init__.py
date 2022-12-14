import os
import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String, UniqueConstraint, create_engine
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import declarative_base, sessionmaker

from app.config.database import SQLALCHEMY_URL

engine = create_engine(SQLALCHEMY_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()


class BaseColumns:
    id = Column(UUID(as_uuid=True), default=uuid.uuid4, primary_key=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    created_by = Column(String, default=os.getlogin(), nullable=False)
    updated_at = Column(DateTime, onupdate=datetime.utcnow)
    updated_by = Column(String, onupdate=os.getlogin())
    UniqueConstraint(id)
