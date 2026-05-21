from pydantic import BaseModel
from typing import Optional
class TaskSchema(BaseModel):
    title: str
    description: str
    is_completed: bool = False

