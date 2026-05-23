from sqlalchemy.orm import Session
from src.users.dtos import UserSchema
def register_user(body:UserSchema,db:Session):
    print(body)
    return{
        "message":"Register Done"
    }