from fastapi import APIRouter, FastAPI
import customer
import organization
from model import *

api_router = APIRouter()

endpoints = [customer, organization]

for endpoint in endpoints:
    api_router.include_router(endpoint.router)

app = FastAPI()

app.include_router(api_router)
