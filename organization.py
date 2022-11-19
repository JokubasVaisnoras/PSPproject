from fastapi import Body, APIRouter
from model import Organization, Order
import coupon
import service
import transaction
import employee
import reservation

router = APIRouter(
    prefix="/organizations/{organization_id}"
)

router.include_router(coupon.router)
router.include_router(service.router)
router.include_router(transaction.router)
router.include_router(employee.router)
router.include_router(reservation.router)


@router.post("/addLocation", tags=["Organizations"], response_model=Organization)
async def add_location(note: str = Body({"location": "Test street 1"})) -> Organization:
    return None


@router.post("/addBankCredentials", tags=["Organizations"], response_model=Organization)
async def add_bank_credentials(note: str = Body({"account_number": "LT0000000000000222"})) -> Organization:
    return None


@router.post("/addWorkingHours", tags=["Organizations"], response_model=Organization)
async def add_opening_time(note: str = Body({"opening": 10, "closing": 22})) -> Organization:
    return None


@router.delete("/", tags=["Organizations"], status_code=204)
async def delete_organization():
    return None


@router.get("/order_history", tags=["Organizations"], response_model=list[Order])
async def get_order_history(organization_id: int) -> list[Order]:
    return None


@router.get("/order_history/{employee_id}", tags=["Organizations"], response_model=list[Order])
async def get_employee_order_history(organization_id: int, employee_id: int) -> list[Order]:
    return None
