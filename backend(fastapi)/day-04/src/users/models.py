from sqlalchemy import Column,String,Integer
from src.config.db import Base

class UserModel(Base):
    __tablename__="users"

    id=Column(Integer,primary_key=True)
    user_name=Column(String(100),unique=True,nullable=True)
    email=Column(String(250),unique=True,nullable=True)
    password=Column(String(250),unique=True,nullable=True)

    