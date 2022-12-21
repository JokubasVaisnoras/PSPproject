from pydantic import BaseModel
from enum import Enum
from typing import List
import datetime
import uuid

## Menu
class MenuBase(BaseModel):
    restaurantId: uuid.UUID
    name: str


class MenuCreate(MenuBase):
    pass


class Menu(MenuBase):
    id: uuid.UUID

    class Config:
        orm_mode = True


class MenuGetPaginated(BaseModel):
    totalPages: int
    items: List[Menu]
##

## Products
class MeasuringTypeEnum(str, Enum):
    kg = "kg"
    g = "g"
    l = "l"
    ml = "ml"
    unit = "unit"
class ProductBase(BaseModel):
    name: str
    measuringType: MeasuringTypeEnum
    amount: int
    price: float

    
class ProductCreate(ProductBase):
    pass
class Product(ProductBase):
    id: uuid.UUID
    restaurantId: uuid.UUID
    class Config:
        orm_mode = True

class ProductGetPaginated(BaseModel):
    totalPages: int
    items: List[Product]

class PaymentBase(BaseModel):
    price: float
    taxAmount: float
    tips: float
    cardId: str
    paymentType: str
    paymentDate: datetime.datetime

class PaymentWithId(PaymentBase):
    id: uuid.UUID
class Payment(PaymentWithId):
    orderId: uuid.UUID
    class Config:
        orm_mode = True

class PaymentCreate(PaymentBase):
    pass

class RecipeBase(BaseModel):
    productId: uuid.UUID
    amount: float
    measuringType: MeasuringTypeEnum

class RecipeWithId(RecipeBase):
    menuItemId: uuid.UUID
class Recipe(RecipeWithId):
    id: uuid.UUID
    class Config:
        orm_mode = True

class RecipeCreate(RecipeBase):
    pass
