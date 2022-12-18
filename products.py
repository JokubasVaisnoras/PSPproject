import schema
import model
from fastapi import APIRouter, Depends, HTTPException, Response
import datetime
import database
import uuid
import re

router = APIRouter(
    prefix="/products",
    tags=["products"]
)


def filterNames(products: list[model.Product], name: str) -> list[model.Product]:
    newList = []
    for product in products:
        if name in product.name:
            newList.append(product)
    return newList

def filterMeasuringTypes(products: list[model.Product], measuringType: model.MeasuringTypeEnum) -> list[model.Product]:
    newList = []
    for product in products:
        if measuringType == product.measuringType:
            newList.append(product)
    return newList

def filterAmount(products: list[model.Product], query: str) -> list[model.Product]:
    number = int(''.join(c for c in query if c.isdigit()))
    newList = []
    if ">" in query:
        if "=" in query:
            for product in products:
                if product.amount >= number:
                    newList.append(product)
        else:
            for product in products:
                if product.amount > number:
                    newList.append(product)
    elif "<" in query:
        if "=" in query:
            for product in products:
                if product.amount <= number:
                    newList.append(product)
        else:
            for product in products:
                if product.amount < number:
                    newList.append(product)
    elif "=" in query:
        for product in products:
                if product.amount == number:
                    newList.append(product)
    return newList

def filterPrice(products: list[model.Product], query: str) -> list[model.Product]:
    number = float(re.sub("[^\d\.]", "", query))
    newList = []
    if ">" in query:
        if "=" in query:
            for product in products:
                if product.price >= number:
                    newList.append(product)
        else:
            for product in products:
                if product.price > number:
                    newList.append(product)
    elif "<" in query:
        if "=" in query:
            for product in products:
                if product.price <= number:
                    newList.append(product)
        else:
            for product in products:
                if product.price < number:
                    newList.append(product)
    elif "=" in query:
        for product in products:
                if product.price == number:
                    newList.append(product)
    return newList

@router.get("/restaurant/{restaurantId}/paginated", response_model=schema.ProductGetPaginated)
async def get_product(restaurantId: uuid.UUID, name: str | None = None, measuringType: model.MeasuringTypeEnum | None = None, amount: str | None = None, 
price: str | None = None, page: int | None = None, db: database.SessionLocal = Depends(database.get_db)):
    arguments = locals()
        
    products = db.query(model.Product).all()
    
    for arg in arguments.items():
        if arg[1] != None:
            if arg[0] == 'name':
                products = filterNames(products=products, name=name)
            if arg[0] == 'measuringType':
                products = filterMeasuringTypes(products=products, measuringType=measuringType)
            if arg[0] == 'amount':
                amountCopy = amount
                pattern = re.compile("/(=|>|<|>=|<|<=|<>)\d+")
                if(pattern.match(amountCopy)):
                    raise HTTPException(status_code=400, detail="Bad amount parameters")
                products = filterAmount(products=products, query=amount)
            if arg[0] == 'price':
                priceCopy = price
                pattern = re.compile("/(=|>|<|>=|<|<=|<>)\d+")
                if(pattern.match(priceCopy)):
                    raise HTTPException(status_code=400, detail="Bad price parameters")
                products = filterPrice(products=products, query=price)
            if arg[0] == 'page':
                if page != 1:
                    products = []
    return schema.ProductGetPaginated(totalPages=1, items=products)



@router.post("/restaurant/{restaurantId}", response_model=schema.Product)
def create_menu(restaurantIdPar: uuid.UUID, product: schema.ProductCreate, db: database.SessionLocal = Depends(database.get_db)):
    db_product = model.Product(restaurantId=restaurantIdPar, name=product.name, measuringType=product.measuringType, amount=product.amount, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# @router.put("/{productId}", tags=["products"], status_code=204)
# async def put_product(productId: str, product: Product):
#     return None #204




# @router.post("/addWorkingHours", tags=["Organizations"], response_model=Organization)
# async def add_opening_time(note: str = Body({"opening": 10, "closing": 22})) -> Organization:
#     return None


# @router.delete("/", tags=["Organizations"], status_code=204)
# async def delete_organization():
#     return None


# @router.get("/order_history", tags=["Organizations"], response_model=list[Order])
# async def get_order_history(organization_id: int) -> list[Order]:
#     return None


# @router.get("/order_history/{employee_id}", tags=["Organizations"], response_model=list[Order])
# async def get_employee_order_history(organization_id: int, employee_id: int) -> list[Order]:
#     return None
