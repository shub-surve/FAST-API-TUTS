from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

# SQLite file path
DATABASE_URL = "sqlite:///./proj.db"  # Fixed URL format

# Create the database engine
Engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create the declarative Base
Base = declarative_base()

