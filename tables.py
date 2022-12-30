from fastapi import APIRouter, Depends, HTTPException, Response
import schema
import uuid
import database
import model

router = APIRouter(
    prefix="/tables",
    tags=["Tables"]
)

@router.get("/restaurant/{restaurantId}/paginated", response_model=schema.TablePaginated)
def get_order_paginated(restaurantId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):

    order = db.query(model.Table).filter(model.Table.id == restaurantId).all()
    return schema.TablePaginated(totalPages=1, id=restaurantId, items=order)


@router.post("/restaurant/{tableId}", response_model=schema.Table)
def create_table_for_restaurant(restaurantId: uuid.UUID, table: schema.Table, db: database.SessionLocal = Depends(database.get_db)):
    db_table_item = model.Table(id= restaurantId, waiterId=table.waiterId, seats=table.seats, status=table.status)
    db.add(db_table_item)
    db.commit()
    db.refresh(db_table_item)
    return db_table_item

@router.put("/{tableId}",status_code=204)
def update_single_table(tableId: uuid.UUID, info: schema.Table,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Table).filter(model.Table.id == tableId).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Table not found")
    db_info.id = info.id
    db_info.waiterId = info.waiterId
    db_info.seats = info.seats
    db_info.status = info.status
    # db.add(db_info)s
    db.commit()

    return Response(status_code=204)

@router.delete("/{tableId}", status_code=204)
def delete_single_table(tableId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Table).filter(model.Table.id == tableId).first()
    if db_info is None:
        return Response(status_code=500)
    db.delete(db_info)
    db.commit()
    return Response(status_code=204)

@router.patch("/{tableId}/status",status_code=204)
def change_single_table_status(tableId:uuid.UUID, status:str, db: database.SessionLocal = Depends(database.get_db)):
    db_status = db.query(model.Table).filter(model.Table.id == tableId).first()
    if db_status is None:
        raise HTTPException(status_code=404, detail="Table not found")
    db_status.status = status
    db.commit()
    return Response(status_code=204)