from fastapi import APIRouter
from model import Discount, Coupon, DiscountType
import datetime

router = APIRouter(
    prefix="/coupons",
    tags=["Coupons"]
)


@router.post("/", response_model=Discount)
async def create_coupon(organization_id: int, coupon: Discount) -> Discount:
    return None


@router.put("/{coupon_id}", response_model=Discount)
async def update_coupon(organization_id: int, coupon_id: int, discount: DiscountType, amount: int) -> Discount:
    return None


@router.post("/{coupon_id}/assign", response_model=Coupon)
async def assign_coupon(organization_id: int, coupon_id: int, customer_id: int, end_date: datetime.datetime) -> Coupon:
    return None
