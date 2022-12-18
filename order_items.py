import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid

router = APIRouter(
    prefix="/order-items",
    tags=["order-items"]
)



@router.get("/restaurant/{restaurantId}/paginated", response_model=schema.OrderItemWithId)
def get_order_paginated(restaurantId: uuid.UUID, status: str | None = None,startDate: datetime.datetime | None = None, endDate: datetime.datetime | None = None, page: int | None = None, db: database.SessionLocal = Depends(database.get_db)):
    order = db.query(model.Order_Item).all()
    return schema.OrderItemWithId(totalPages=1, id=restaurantId, items=order)


@router.post("/restaurant/{restaurantId}", response_model=schema.OrderItem)
def post_order_item(restaurantId: uuid.UUID, order: schema.OrderItem, db: database.SessionLocal = Depends(database.get_db)):
    db_order_item = model.Order_Item(id=restaurantId, comment = order.comment, orderId= order.orderId, menuItem=order.menuItem, quantity=order.quantity, status= order.status, startDate= order.startDate, endDate=order.endDate)
    db.add(db_order_item)
    db.commit()
    db.refresh(db_order_item)
    return db_order_item

@router.patch("/{orderItemId}/recipe",status_code=204)
def patch_menu(orderItemId:uuid.UUID, status:str, db: database.SessionLocal = Depends(database.get_db)):
    db_status = db.query(model.Order_Item).filter(model.Order_Item.id == orderItemId).first()
    if db_status is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    db_status.status = status
    db.commit()
    return Response(status_code=204)


@router.get("/{orderItemId}", response_model=schema.OrderItemWithId)
def get_order(orderItemId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    order = db.query(model.Order_Item).filter(model.Order_Item.orderId == orderItemId)
    return schema.OrderItem(items=order)

@router.put("/{orderItemId}",status_code=204)
def put_order_item(orderItemId: uuid.UUID, info: schema.OrderItemCreate,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Order_Item).filter(model.Order_Item.id == orderItemId).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    db_info.orderId = info.orderId
    db_info.menuItem = info.menuItem
    db_info.quantity = info.quantity
    db_info.status = info.status
    db_info.comment = info.comment
    db_info.startDate = info.startDate
    db_info.endDate = info.endDate
    # db.add(db_info)s
    db.commit()

    return Response(status_code=204)


@router.delete("/{orderItemId}", status_code=204)
def delete_order_item(orderItemId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Order_Item).filter(model.Order_Item.id == orderItemId).first()
    if db_info is None:
        return Response(status_code=500)
    db.delete(db_info)
    db.commit()
    return Response(status_code=204)

# @router.put("/{menuId}", status_code=204)
# def update_menu(menuId: uuid.UUID, menu: schema.MenuCreate, db: database.SessionLocal = Depends(database.get_db)):
#     db_menu = db.query(model.Menu).filter(model.Menu.id == menuId).first()
#     if db_menu is None:
#         raise HTTPException(status_code=404, detail="Menu not found")
#     db_menu.restaurantId = menu.restaurantId
#     db_menu.name = menu.name
#     db.commit()
#     return Response(status_code=204)



