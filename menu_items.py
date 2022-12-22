import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid
import re
from dateutil import parser

router = APIRouter(
    prefix="/menu-items",
    tags=["menu-items"]
)



@router.post("/menu/{menuId}", response_model=schema.MenuItem)
def post_menu_item(menuId: uuid.UUID, menu: schema.MenuItem, db: database.SessionLocal = Depends(database.get_db)):
    db_menu_item = model.MenuItem(id= menuId, recipeId=menu.recipeId, description=menu.description, photo=menu.photo, cookingDescription=menu.cookingDescription, state=menu.state, defaultDiscount=menu.defaultDiscount, loyaltyDiscount=menu.loyaltyDiscount, price=menu.price )
    db.add(db_menu_item)
    db.commit()
    db.refresh(db_menu_item)
    return db_menu_item

# @router.patch("/{orderItemId}/recipe",status_code=204)
# def patch_menu(orderItemId:uuid.UUID, status:str, db: database.SessionLocal = Depends(database.get_db)):
#     db_status = db.query(model.Order_Item).filter(model.Order_Item.id == orderItemId).first()
#     if db_status is None:
#         raise HTTPException(status_code=404, detail="Menu not found")
#     db_status.status = status
#     db.commit()
#     return Response(status_code=204)


@router.get("/{menuItemId}", response_model=schema.MenuItemModel)
def get_menu(menuItemId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    menu = db.query(model.MenuItem).filter(model.MenuItem.id  == menuItemId).first()
    if menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    return schema.MenuItemModel(items=menu)

@router.put("/{menuItemId}",status_code=204)
def updates_single_menu_item(menuItedId: uuid.UUID, info: schema.MenuItem,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.MenuItem).filter(model.MenuItem.id == menuItedId).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    db_info.recipeId = info.recipeId
    db_info.description = info.description
    db_info.photo = info.photo
    db_info.cookingDescription = info.cookingDescription
    db_info.state = info.state
    db_info.defaultDiscount = info.defaultDiscount
    db_info.loyaltyDiscount = info.loyaltyDiscount
    db_info.price = info.price
    # db.add(db_info)s
    db.commit()

    return Response(status_code=204)


@router.delete("/{menuItemId}", status_code=204)
def deletes_single_menu_item(menuItemId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.MenuItem).filter(model.MenuItem.id == menuItemId).first()
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



