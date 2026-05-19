from sqlalchemy import Column,Integer,String,Boolean
from src.config.db import Base


class TaskModel(Base):
    __tablename__="user_task"

    id=Column(Integer,primary_key=True)
    title=Column(String,nullable=False)
    description=Column(String,nullable=False)
    is_completed=Column(Boolean,default=False)