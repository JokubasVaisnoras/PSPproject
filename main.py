from fastapi import APIRouter, FastAPI, Depends, HTTPException
import customer
import organization
from model import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

# Set up database
engine = create_engine("postgresql+psycopg2://user:password@postgresql:5432")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define database model


class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)


Base.metadata.create_all(bind=engine)

api_router = APIRouter()

# Define request model


class TaskCreate(BaseModel):
    title: str
    description: str


api_router.include_router(customer.router)
api_router.include_router(organization.router)

app = FastAPI()

# Define a function to get a database session


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

# Define a route to create a new task


@app.post("/tasks")
def create_task(task: TaskCreate, db: SessionLocal = Depends(get_db)):
    new_task = Task(title=task.title, description=task.description)
    db.add(new_task)
    db.commit()
    db.refresh(new_task)
    return new_task


# Define a route to get a task
@app.get("/tasks/{task_id}")
def get_task(task_id: int, db: SessionLocal = Depends(get_db)):
    task = db.query(Task).filter(Task.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


app.include_router(api_router)

print("\nDocs available from:", flush=True)
print("http://localhost:8000/redoc", flush=True)
print("http://localhost:8000/docs\n", flush=True)
