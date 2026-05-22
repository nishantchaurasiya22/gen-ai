from src.tasks.dtos import TaskSchema,TaskResponseSchema
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.tasks.models import TaskModel
def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task=TaskModel(
        title=data["title"],
        description=data["description"],
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task

def get_tasks(db:Session):
    all_tasks=db.query(TaskModel).all()
    return all_tasks

def get_task(task_id:int,db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="Task not found")
    return one_task

def update_task(task_id:int,body:TaskSchema,db:Session):
    update_task=db.query(TaskModel).get(task_id)
    if not update_task:
        raise HTTPException(status_code=404,detail="task not found")
    body=body.model_dump()
    for field,value in body.items():
        setattr(update_task,field,value)
    db.add(update_task)
    db.commit()
    db.refresh(update_task)

    return update_task

def delete_task(task_id:int,db:Session):
    delete_task=db.query(TaskModel).get(task_id)
    if not delete_task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(delete_task)
    db.commit()
    return None
