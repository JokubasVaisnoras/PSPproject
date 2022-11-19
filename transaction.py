from fastapi import APIRouter
from model import Transaction, TransactionType

router = APIRouter(
    prefix="/transactions",
    tags=["Transactions"]
)


@router.get("/transactions", response_model=list[Transaction])
async def get_transactions(organization_id: int) -> list[Transaction]:
    return None


@router.post("/transactions", response_model=list[Transaction])
async def get_filtered_transactions(organization_id: int, filters: list[TransactionType]) -> list[Transaction]:
    return None
