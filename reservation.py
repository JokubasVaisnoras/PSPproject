from fastapi import APIRouter
from model import OrderedService

router = APIRouter(
    prefix="/reservations",
    tags=["Reservations"]
)


@router.put("/{reservation_id}/handle", response_model=OrderedService)
async def handle_reservation() -> OrderedService:
    return None


@router.post("/{reservation_id}/addNote", response_model=OrderedService)
async def add_note(note: str) -> OrderedService:
    return None
