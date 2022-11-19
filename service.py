from fastapi import APIRouter
from model import Service, OrderedService, Discount

router = APIRouter(
    prefix="/services",
    tags=["Services"]
)


@router.put("/{service_id}/discounts", response_model=Discount)
async def add_discounts(organization_id: int, service_id: int) -> Discount:
    return None


@router.post("/", response_model=Service)
async def add_service() -> Service:
    return None


@router.delete("/{service_id}", status_code=204)
async def remove_service(organization_id: int, service_id: int) -> None:
    return None


@router.get("/search", response_model=list[Service])
async def search_services(name: str) -> list[Service]:
    return None


@router.put("/{service_id}/reserve", response_model=OrderedService)
async def reserve_service() -> OrderedService:
    return None
