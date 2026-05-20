from sqlalchemy import Column,Integer,Boolean,String
from src.config.db import Base
class TaskModel(Base):
    __tablename__="user_task"

    id=Column(Integer,primary_key=True)
    title=Column(String(100),nullable=False)
    description=Column(String(500),nullable=False)
    is_completed=Column(Boolean, default=False)