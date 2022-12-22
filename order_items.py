import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid
import re
from dateutil import parser

router = APIRouter(
    prefix="/order-items",
    tags=["order-items"]
)
def filterStatus(orders:list[model.Order_Item], status: str):
    newList = []
    print(orders)
    for order in orders:
        print("order",order, "order status:",order.status.value)
        if status == order.status.value:
            newList.append(order)
            print(order)
    return newList

def filterStartDate(orders:list[model.Order_Item], query: str, onlyDate: datetime.datetime, date:str):
    # number = int(''.join(c for c in query if c.isdigit()))

    newList = []
    if ">" in query:
        if "=" in query:
            for order in orders:
                if order.startDate.timestamp() >= onlyDate:
                    newList.append(order)
        else:
            for order in orders:
                if order.startDate.timestamp() > onlyDate:
                    newList.append(order)
    elif "<" in query:
        if "=" in query:
            for order in orders:
                if order.startDate.timestamp() <= onlyDate:
                    newList.append(order)
        else:
            for order in orders:
                if order.startDate.timestamp() < onlyDate:
                    newList.append(order)
    elif "=" in query:
        for order in orders:
            if order.startDate.timestamp() == onlyDate :
                newList.append(order)
    return newList

def filterEndDate(orders:list[model.Order_Item], query: str, onlyDate: datetime.datetime, date:str):
    # number = int(''.join(c for c in query if c.isdigit()))

    newList = []
    if ">" in query:
        if "=" in query:
            for order in orders:
                if order.endDate.timestamp() >= onlyDate:
                    newList.append(order)
        else:
            for order in orders:
                if order.endDate.timestamp() > onlyDate:
                    newList.append(order)
    elif "<" in query:
        if "=" in query:
            for order in orders:
                if order.endDate.timestamp() <= onlyDate:
                    newList.append(order)
        else:
            for order in orders:
                if order.endDate.timestamp() < onlyDate:
                    newList.append(order)
    elif "=" in query:
        for order in orders:
            if order.endDate.timestamp() == onlyDate :
                newList.append(order)
    return newList

# def filterPrice(orders: list[model.Order_Item], query: str) -> list[model.Order_Item]:
#     number = float(re.sub("[^\d\.]", "", query))
#     newList = []
#     if ">" in query:
#         if "=" in query:
#             for order in orders:
#                 if order.price >= number:
#                     newList.append(order)
#         else:
#             for order in orders:
#                 if order.price > number:
#                     newList.append(order)
#     elif "<" in query:
#         if "=" in query:
#             for order in orders:
#                 if order.price <= number:
#                     newList.append(order)
#         else:
#             for order in orders:
#                 if order.price < number:
#                     newList.append(order)
#     elif "=" in query:
#         for order in orders:
#                 if order.price == number:
#                     newList.append(order)
#     return newList



@router.get("/restaurant/{restaurantId}/paginated", response_model=schema.OrderItemWithId)
def get_order_paginated(restaurantId: uuid.UUID, status: str | None = None,startDate: str | None = None, endDate: str | None = None, page: int | None = None, db: database.SessionLocal = Depends(database.get_db)):
    arguments = locals()
    order = db.query(model.Order_Item).filter(model.Order_Item.id == restaurantId).all()
    
    for arg in arguments.items():
        if arg[1] != None:
            if arg[0] == 'status':
                order = filterStatus(orders=order, status=status)
            if arg[0] == 'startDate':
                startDateCopy = startDate
                # pattern = re.compile("[=<>]")
                # if(pattern.match(startDateCopy)):
                #     raise HTTPException(status_code=400, detail="Bad parameters")
                onlyDate = re.split(r"[=<>]", startDate)
                date = parser.parse(onlyDate[1])
                date = date.timestamp()
                order = filterStartDate(orders=order, query=startDate, onlyDate=date, date='startDate')
            if arg[0] == 'endDate':
                dateCopy = startDate
                # pattern = re.compile("[=<>]")
                # if(pattern.match(dateCopy)):
                #     raise HTTPException(status_code=400, detail="Bad price parameters")
                onlyDate = re.split(r"[=<>]", startDate)
                date = parser.parse(onlyDate[1])
                date = date.timestamp()
                order = filterEndDate(orders=order, query=endDate, onlyDate=date, date='endDate')
            if arg[0] == 'page':
                if page != 1:
                    order = []
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
    # order = db.query(model.Order_Item).filter(model.Order_Item.orderId == orderItemId)
    order = db.query(model.Order_Item).filter(model.Order_Item.id == orderItemId).all()

    return schema.OrderItemWithId(items=order, totalPages=1)

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



