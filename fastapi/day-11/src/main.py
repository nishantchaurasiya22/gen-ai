from fastapi import FastAPI
from src.config.db import base,engine
from src.tasks.routes import task_routes
from src.tasks.models import TaskModel
base.metadata.create_all(engine)
app=FastAPI()

@app.get("/")
def root():
    return{
        "message":"hello from fastapi"
    }
app.include_router(task_routes)