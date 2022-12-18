from fastapi import APIRouter, FastAPI, Depends, HTTPException
import customer
import organization
import database
import menu, order_items
from model import *
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

database.Base.metadata.create_all(bind=database.engine)

api_router = APIRouter()

api_router.include_router(customer.router)
api_router.include_router(organization.router)


api_router.include_router(menu.router)
api_router.include_router(order_items.router)

app = FastAPI()


app.include_router(api_router)

print("\nDocs available from:", flush=True)
print("http://localhost:8000/redoc", flush=True)
print("http://localhost:8000/docs\n", flush=True)
