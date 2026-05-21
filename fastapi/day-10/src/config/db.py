from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
from src.config.settings import settings 
Base=declarative_base()
engine=create_engine(settings.DATABASE_URL)
LocalSession=sessionmaker(bind=engine)

def get_db():
    setting=LocalSession()
    try:
        yield setting
    finally:
        setting.close()
    

