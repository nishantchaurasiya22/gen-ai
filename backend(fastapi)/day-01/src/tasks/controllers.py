from src.tasks.dtos import TaskSchema
from src.tasks.models import TaskModel
from fastapi import HTTPException
from sqlalchemy.orm import Session
def create_task(body:TaskSchema,db:Session):
    data=body.model_dump()
    new_task=TaskModel(
        title=data['title'],
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
    task=db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    return task

def update_task(task_id:int,body:TaskSchema,db:Session):
    task=db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    body=body.model_dump()
    for field,value in body.items():
        setattr(task,field,value)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

def delete_task(task_id:int,db:Session):
    task=db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(status_code=404,detail="Task not found")
    db.delete(task)
    db.commit()
    return None