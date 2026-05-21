from fastapi import APIRouter,Depends
from src.config.db import get_db
from src.tasks import controllers
from src.tasks.dtos import TaskSchema
task_route=APIRouter(prefix="/tasks")

@task_route.post("/create")
def create_tasks(body:TaskSchema,db=Depends(get_db)):
    return controllers.create_task(body,db)

@task_route.get("/all_tasks")
def get_tasks(db=Depends(get_db)):
    return controllers.get_tasks(db)

@task_route.get("/one_task/{task_id}")
def one_task(task_id:int,db=Depends(get_db)):
    return controllers.get_one_task(task_id,db)

@task_route.put("/update_task/{task_id}")
def update_task(task_id:int,body:TaskSchema,db=Depends(get_db)):
    return controllers.update_task(task_id,body,db)


@task_route.delete("/delete_task/{task_id}")
def delete_task(task_id:int,db=Depends(get_db)):
    return controllers.delete_task(task_id,db)
                