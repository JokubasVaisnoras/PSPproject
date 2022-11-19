from fastapi import APIRouter
from model import OrderedService
import datetime

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.put("/{reservation_id}", response_model=OrderedService)
async def update_reservation() -> OrderedService:
    return None


@router.put("/{reservation_id}/handle", response_model=OrderedService)
async def handle_reservation() -> OrderedService:
    return None


@router.put("/{reservation_id}/addNote", response_model=OrderedService)
async def add_note(note: str) -> OrderedService:
    return None


@router.put("/{reservation_id}/setEstimate", response_model=OrderedService)
async def set_estimate(estimate: datetime.datetime) -> OrderedService:
    return None


@router.put("/{reservation_id}/setStatus", response_model=OrderedService)
async def set_status() -> OrderedService:
    return None


@router.put("/{reservation_id}/payCash", response_model=OrderedService)
async def pay_cash() -> OrderedService:
    return None


@router.put("/{reservation_id}/payLoyalty", response_model=OrderedService)
async def pay_loyalty() -> OrderedService:
    return None


@router.get("/{reservation_id}/receipt", response_model=str)
async def get_receipt() -> str:
    return None
