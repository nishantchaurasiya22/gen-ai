from src.tasks.dtos import TaskSchema
from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.tasks.models import TaskModel
def create_task(body:TaskSchema, db=Session):
    data=body.model_dump()
    new_task=TaskModel(
        title=data["title"],
        description=data["description"]
    )
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return{
        "status":"Task created successfully",
        "data":new_task
    }

def get_tasks(db:Session):
    tasks=db.query(TaskModel).all()
    return{
        "status":"Tasks fetching successfully",
        "data":tasks
    }

def get_one_task(task_id:int, db:Session):
    one_task=db.query(TaskModel).get(task_id)
    if not one_task:
        raise HTTPException(status_code=404,detail="task not found")
    return{
        "status":"task fetching successfully",
        "data":one_task
    }

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

    return{
        "status":"updated task successfully",
        "data":update_task
    }

def delete_task(task_id:int, db:Session):
    delete_task=db.get(TaskModel,task_id)
    if not delete_task:
        raise HTTPException(status_code=404,detail="task not found")
    db.delete(delete_task)
    db.commit()
    
    return{
        "status":"Task deleted successfully"
    }