from fastapi import APIRouter, Depends, HTTPException, Response
import schema
import uuid
import database
import model

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)



@router.post("/restaurant/{orderId}", response_model=schema.Order)
def create_order_for_table(orderId: uuid.UUID, order:schema.Order, db: database.SessionLocal = Depends(database.get_db)):
    db_table_item = model.Order(orderId = orderId, tableId=order.tableId, cashierId=order.cashierId, partnerId=order.partnerId, orderType=order.orderType, totalPrice=order.totalPrice, taxType=order.taxType, date=order.date, tips=order.tips)
    db.add(db_table_item)
    db.commit()
    db.refresh(db_table_item)
    return db_table_item

@router.get("/{orderId}}", response_model=schema.OrderListed)
def return_single_order(orderId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):

    order = db.query(model.Order).filter(model.Order.orderId == orderId).all()
    if order is None:
        raise HTTPException(status_code=404, detail="Order not found")
    return schema.OrderListed(order = order)


@router.put("/{orderId}",status_code=204)
def update_single_order(orderId: uuid.UUID, info: schema.Order,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Order).filter(model.Order.orderId == orderId).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Order not found")
    db_info.tableId = info.tableId
    db_info.cashierId = info.cashierId
    db_info.partnerId = info.partnerId
    db_info.orderType = info.orderType
    db_info.totalPrice = info.totalPrice
    db_info.taxType = info.taxType
    db_info.date = info.date
    db_info.tips = info.tips
    # db.add(db_info)s
    db.commit()

    return Response(status_code=204)

@router.delete("/{orderId}", status_code=204)
def delete_single_order(orderId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Order).filter(model.Order.orderId == orderId).first()
    if db_info is None:
        return Response(status_code=500)
    db.delete(db_info)
    db.commit()
    return Response(status_code=204)