from fastapi import APIRouter,Depends
from src.config.db import get_db
from src.tasks import controllers
from src.tasks.dtos import TaskSchema
task_routes=APIRouter(prefix="/tasks")
@task_routes.post("/create")
def create_task(body:TaskSchema,db=Depends(get_db)):
    return controllers.create_task(body,db)

@task_routes.get("/get_tasks")
def get_tasks(db=Depends(get_db)):
    return controllers.get_tasks(db)
