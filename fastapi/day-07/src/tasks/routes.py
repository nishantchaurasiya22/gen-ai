from fastapi import APIRouter,Depends
from src.tasks import controllers
from src.config.db import get_db
from src.tasks.dtos import TaskSchema
task_routes=APIRouter(prefix="/tasks")
@task_routes.post("/create")
def create_task(body:TaskSchema, db=Depends(get_db) ):
    return controllers.create_task(body,db)