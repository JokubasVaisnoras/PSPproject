from fastapi import APIRouter, FastAPI, HTTPException
import database
import menu
import products
import payments
import recipe
from model import *
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

database.Base.metadata.create_all(bind=database.engine)

api_router = APIRouter()

api_router.include_router(menu.router)
api_router.include_router(products.router)
api_router.include_router(payments.router)
api_router.include_router(recipe.router)

app = FastAPI()

app.include_router(api_router)

print("\nDocs available from:", flush=True)
print("http://localhost:8000/redoc", flush=True)
print("http://localhost:8000/docs\n", flush=True)
