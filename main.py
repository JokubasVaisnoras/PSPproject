from fastapi import Body, FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

tags_metadata = [
    {
        "name": "services",
        "description": "Operations with services.",
    },
]


class Organization(BaseModel):
    id: int
    name: str
    credentials: dict
    settings: dict
    created_timestamp: int
    opening: int
    closing: int


class Service(BaseModel):
    id: int
    org_id: int
    price: int
    description: str
    created_timestamp: int
    available: bool


class OrderedService(BaseModel):
    id: int
    order_id: int
    service_id: int
    created_timestamp: int

class Discount(BaseModel):
    id:int
    service_id:int
    percentage_off:int
    exact_price:int
    created_timestamp:datetime.datetime

class User(BaseModel):
    id: int
    password: str
    email: str
    full_name: str
    created_date: datetime.datetime
    phonenumber: str
    

@app.get("/organizations/{organization_id}/services/search", tags=["services"], response_model=list[Service])
async def search_services(name: str) -> list[Service]:
    return None


@app.put("/organizations/{organization_id}/services/{service_id}/reserve", tags=["services"], response_model=OrderedService)
async def reserve_service() -> OrderedService:
    return None


@app.put("/organizations/{organization_id}/reservations/{reservation_id}/handle", tags=["services"], response_model=OrderedService)
async def handle_reservation() -> OrderedService:
    return None


@app.post("/organizations/{organization_id}/reservations/{reservation_id}/addnote", tags=["services"], response_model=OrderedService)
async def reservation_add_note(note: str = Body()) -> OrderedService:
    return None


@app.post("/organizations/{organization_id}/services/add", tags=["services"], response_model=Service)
async def add_service() -> Service:
    return None


@app.delete("/organizations/{organization_id}/services/{service_id}/remove", tags=["services"])
async def remove_service(organization_id:int,service_id:int) -> None:
    return "succesful"


@app.put("/organizations/{organization_id}/services/{service_id}/discounts", tags=["services"],response_model=Discount)
async def remove_service(organization_id:int,service_id:int) -> Discount:
    return None

@app.post("/customers/user/add", tags=["Customer"],response_model=User)
async def create_account() -> User:
    return None

@app.get("/customers/{customer_id}/info", tags=["Customer"],response_model=User)
async def check_information(customer_id:int) -> User:
    return None

@app.put("/customers/{customer_id}/info", tags=["Customer"],response_model=User)
async def update_information(customer_id:int) -> User:
    return None