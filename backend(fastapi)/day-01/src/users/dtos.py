from pydantic import BaseModel
class UserSchema(BaseModel):      # register ke liye
    username: str
    email: str
    hash_password: str  
    