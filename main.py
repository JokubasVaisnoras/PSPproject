from fastapi import Body, FastAPI
from pydantic import BaseModel

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
