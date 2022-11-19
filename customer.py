from fastapi import APIRouter
from model import User

router = APIRouter(
    prefix="/customers",
    tags=["Customers"]
)


@router.post("/", response_model=User)
async def create_customer() -> User:
    return None


@router.put("/{customer_id}", response_model=User)
async def update_customer(customer_id: int) -> User:
    return None


@router.get("/{customer_id}", response_model=User)
async def get_customer(customer_id: int) -> User:
    return None


@router.delete("/{customer_id}", status_code=204)
async def delete_customer():
    return None
