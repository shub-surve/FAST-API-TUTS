from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker

from core.cfg import Settings

Database_URL = "sqlite:///./my_app.db"
engine = create_engine(Database_URL , connect_args={"check_same_thread": False})




