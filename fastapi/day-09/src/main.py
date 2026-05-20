from fastapi import FastAPI
from src.tasks.models import TaskModel
from src.config.db import Base,engine

from src.tasks.routes import task_routes
app=FastAPI()
Base.metadata.create_all(engine)
@app.get("/")
def root():
    return {"message":"hello,from fastapi"}
app.include_router(task_routes)
