from fastapi import APIRouter,Depends,status
from sqlalchemy.orm import Session
from src.users.dtos import UserSchema
from src.config.db import get_db
from src.users import controllers
user_route=APIRouter(prefix="/auth")
@user_route.post("/register",status_code=status.HTTP_201_CREATED)
def register_user(body:UserSchema,db:Session=Depends(get_db)):
    return controllers.register_user(body,db)
