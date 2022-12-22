import schema
import model
from fastapi import APIRouter, Depends
import database
import uuid

router = APIRouter(
    prefix="/employees",
    tags=["employees"]
)


@router.post("/restaurant/{restaurantId}", response_model=schema.Employee)
def create_menu(restaurantId: uuid.UUID, employee: schema.EmployeeCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_employee = model.Employee(
        id=employee.id,
        name=employee.name,
        lastName=employee.lastName,
        loginCode=employee.loginCode,
        position=employee.position,
        scheduleId=employee.scheduleId,
        salary=employee.salary,
        tipsAmount=employee.tipsAmount
    )
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee
