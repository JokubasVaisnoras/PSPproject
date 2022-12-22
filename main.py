from fastapi import APIRouter, FastAPI
import database
import menu
import order_items
import menu_items
import products
import payments
import recipe
import employee
import shift
from model import *

database.Base.metadata.create_all(bind=database.engine)

api_router = APIRouter()

api_router.include_router(menu.router)
api_router.include_router(order_items.router)
api_router.include_router(menu_items.router)
api_router.include_router(products.router)
api_router.include_router(payments.router)
api_router.include_router(recipe.router)
api_router.include_router(employee.router)
api_router.include_router(shift.router)

app = FastAPI()

app.include_router(api_router)

print("\nDocs available from:", flush=True)
print("http://localhost:8000/redoc", flush=True)
print("http://localhost:8000/docs\n", flush=True)
