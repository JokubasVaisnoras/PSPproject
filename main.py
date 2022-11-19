from fastapi import APIRouter, FastAPI
import customer
import organization
from model import *

api_router = APIRouter()

api_router.include_router(customer.router)
api_router.include_router(organization.router)

app = FastAPI()

app.include_router(api_router)
