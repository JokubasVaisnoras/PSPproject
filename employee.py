from fastapi import Body, APIRouter
from model import Shift, Organization, EmployeeOrganization, Employee, CensoredEmployee

router = APIRouter(
    prefix="/employees",
    tags=["Employees"]
)


@router.post("/", response_model=EmployeeOrganization)
async def add_employee(note: str = Body({"id": 1, "user_id": 15, "org_id": 1337, "access": {"access1": True, "access2": False}})) -> Organization:
    return None


@router.get("/{employee_id}", response_model=Employee)
async def get_employee():
    return None


@router.put("/{employee_id}", response_model=Employee)
async def update_employee(employee_id: int, new_employee: Employee) -> CensoredEmployee:
    return None


@router.delete("/{employee_id}", status_code=204)
async def delete_employee():
    return None


@router.post("/{employee_id}/shifts", response_model=Shift)
async def add_shift(note: str = Body({"id": 1, "emp_org_id": 55, "start_time": "2008-09-15T15:53:00+05:00", "end_time": "2008-10-15T15:53:00+05:00", "created_timestamp": "2007-09-15T15:53:00+05:00"})) -> Organization:
    return None


@router.put("/{employee_id}/shifts/{shift_id}", response_model=Shift)
async def update_shift(note: str = Body({"id": 0, "emp_org_id": 0})) -> Shift:
    return None
