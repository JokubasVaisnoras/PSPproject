import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid
from typing import List

router = APIRouter(
    prefix="/menu-items",
    tags=["recipes"]
)

@router.get("/{menuItemId}/recipe}", response_model=List[schema.RecipeBase])
async def get_recipe(menuItemId: uuid.UUID, db: database.SessionLocal = Depends(database.get_db)):
    recipes = db.query(model.Recipe).filter(model.Recipe.menuItemId == menuItemId).all()
    returnRecipes = []
    for recipe in recipes:
        returnRecipes.append(schema.RecipeBase(productId=recipe.productId, amount=recipe.amount, measuringType=recipe.measuringType))
    return returnRecipes



@router.post("/{menuItemId}}/recipe", response_model=schema.Recipe, status_code=201)
def create_recipe(menuItemId: uuid.UUID, recipe: schema.RecipeCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_recipe = model.Recipe(productId=recipe.productId, menuItemId=menuItemId, amount=recipe.amount, measuringType=recipe.measuringType)
    db.add(db_recipe)
    db.commit()
    db.refresh(db_recipe)
    return db_recipe

@router.put("/{menuItemId}}/recipe",status_code=204)
def put_recipe(menuItemId: uuid.UUID, recipe: schema.RecipeBase,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Recipe).filter(model.Recipe.menuItemId == menuItemId).filter(model.Recipe.productId == recipe.productId).first()
    if db_info is None:
        raise HTTPException(status_code=404, detail="Product not found")
    db_info.amount = recipe.amount
    db_info.measuringType = recipe.measuringType
    # db.add(db_info)s
    db.commit()

    return Response(status_code=204)

@router.delete("/{menuItemId}/recipe}", status_code=204)
def delete_recipe(menuItemId: uuid.UUID,  db: database.SessionLocal = Depends(database.get_db)):
    db_info = db.query(model.Recipe).filter(model.Recipe.menuItemId == menuItemId).all()
    if db_info is None:
        return Response(status_code=500)
    for recipe in db_info:
        db.delete(recipe)
        db.commit()
    return Response(status_code=204)

