from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import UUID
from uuid import uuid4
from sqlalchemy import String

from core.database.base import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(UUID, primary_key=True, default=uuid4)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=False)
