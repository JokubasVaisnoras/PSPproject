import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import database
import uuid

router = APIRouter(
    prefix="/shifts",
    tags=["shifts"]
)


# Page currently ignored
@router.get("/employee/{employeeId}/paginated", response_model=schema.ShiftGetPaginated)
def get_shifts_paginated(employeeId: uuid.UUID, page: int, db: database.SessionLocal = Depends(database.get_db)):
    shifts = db.query(model.Shift).filter(
        model.Shift.employeeId == employeeId).all()
    return schema.ShiftGetPaginated(totalPages=1, items=shifts)


@router.post("/employee/{employeeId}", response_model=schema.Shift)
def create_shift(employeeId: uuid.UUID, shift: schema.ShiftCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_shift = model.Shift(employeeId=employeeId,
                           startTime=shift.startTime,
                           endTime=shift.endTime,
                           date=shift.date
                           )
    db.add(db_shift)
    db.commit()
    db.refresh(db_shift)
    return db_shift


@router.put("/{shiftId}", status_code=204)
def update_shift(shiftId: uuid.UUID, shift: schema.ShiftCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_shift = db.query(model.Shift).filter(model.Shift.id == shiftId).first()
    if db_shift is None:
        raise HTTPException(status_code=404, detail="Shift not found")
    db_shift.startTime = shift.startTime
    db_shift.endTime = shift.endTime
    db_shift.date = shift.date
    db.commit()
    return Response(status_code=204)


@router.delete("/{shiftId}", status_code=204)
def update_shift(shiftId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    db_shift = db.query(model.Shift).filter(model.Shift.id == shiftId).first()
    if db_shift is not None:
        db.delete(db_shift)
        db.commit()
    return Response(status_code=204)
