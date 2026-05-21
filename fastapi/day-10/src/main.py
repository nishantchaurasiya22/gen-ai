from fastapi import FastAPI
from src.tasks.routes import task_route
from src.config.db import Base,engine
Base.metadata.create_all(engine)
app=FastAPI()

@app.get("/")
def root():
    return{
        "details":"hello,from fastapi"
    }

app.include_router(task_route)