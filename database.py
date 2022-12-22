from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2  # Do not delete this

engine = create_engine(
    "postgresql+psycopg2://user:password@postgresql:5432")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


# Define a function to get a database session
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()
