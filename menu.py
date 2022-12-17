import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database


router = APIRouter(
    prefix="/menus",
    tags=["menus"]
)


# Page currently ignored
@router.get("/restaurant/{restaurantId}/paginated")
def get_menus_paginated(restaurantId: str, page: int, db: database.SessionLocal = Depends(database.get_db), response_model=schema.MenuGetPaginated):
    menus = db.query(model.Menu).all()
    return schema.MenuGetPaginated(totalPages=1, items=menus)


# restaurantId both in path and request body
@router.post("/restaurant/{restaurantId}")
def create_menu(restaurantId: str, menu: schema.MenuCreate, db: database.SessionLocal = Depends(database.get_db), response_model=schema.Menu):
    db_menu = model.Menu(restaurantId=menu.restaurantId, name=menu.name)
    db.add(db_menu)
    db.commit()
    db.refresh(db_menu)
    return db_menu


@router.put("/{menuId}")
def update_menu(menuId: str, menu: schema.MenuCreate, db: database.SessionLocal = Depends(database.get_db), status_code=204):
    db_menu = db.query(model.Menu).filter(model.Menu.id == menuId).first()
    if db_menu is None:
        raise HTTPException(status_code=404, detail="Menu not found")
    db_menu.restaurantId = menu.restaurantId
    db_menu.name = menu.name
    db.commit()
    return Response(status_code=204)


@router.delete("/{menuId}")
def update_menu(menuId: str, menu: schema.MenuCreate, db: database.SessionLocal = Depends(database.get_db), status_code=204):
    db_menu = db.query(model.Menu).filter(model.Menu.id == menuId).first()
    if db_menu is None:
        return Response(status_code=204)
    db.delete(db_menu)
    db.commit()
    return Response(status_code=204)
