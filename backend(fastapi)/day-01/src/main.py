from fastapi import FastAPI
from src.tasks.routes import task_route
from src.users.routes import user_route
from src.config.db import engine,base
from src.tasks import models as task_models
from src.users import models as user_models
base.metadata.create_all(engine)
app=FastAPI()
@app.get("/")
def root():
    return{
        "message":"hello,from fastapi"
    }
app.include_router(task_route)
app.include_router(user_route)