from pydantic import BaseModel
from enum import Enum
from typing import List
import datetime
import uuid


# Menu
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
## order-items
# class OrderItemWithID(BaseModel):



class OrderItemStatusEnum(Enum):
    pending = "Pending"
    making = "Making"
    delivering = "Delivering"
    complete = "Complete"

class OrderItem(BaseModel):
    orderId: uuid.UUID
    menuItem: uuid.UUID
    quantity: int
    status: OrderItemStatusEnum
    comment: str
    startDate: datetime.datetime
    endDate: datetime.datetime
    class Config:
        orm_mode = True

class OrderItemWithIdModel(OrderItem):
    id: uuid.UUID


class OrderItemWithId(BaseModel):
    totalPages: int
    items: List[OrderItemWithIdModel]

class OrderItemCreate(OrderItem):
    pass


## menu-items
class MenuItemStateEnum(Enum):
    inStock = "In Stock"
    outOfStock = "Out Of Stock"

class MenuItem(BaseModel):
    recipeId: uuid.UUID
    description: str
    photo: str
    cookingDescription: str
    state: MenuItemStateEnum
    defaultDiscount: float
    loyaltyDiscount: float
    price: float
    class Config:
        orm_mode = True
class MenuItemModel(BaseModel):
    items:MenuItem

class MenuItemWithId(MenuItem):
    id: uuid.UUID




# Employee
class EmployeePositionEnum(str, Enum):
    Waiter = "Waiter"
    Chef = "Chef"
    Administrator = "Administrator"


class EmployeeBase(BaseModel):
    id: uuid.UUID
    name: str
    lastName: str
    loginCode: str
    position: EmployeePositionEnum
    scheduleId: uuid.UUID
    salary: int
    tipsAmount: int


class EmployeeCreate(EmployeeBase):
    pass


class Employee(EmployeeBase):
    class Config:
        orm_mode = True
##


# Shift
class ShiftBase(BaseModel):
    id: uuid.UUID
    startTime: datetime.datetime
    endTime: datetime.datetime
    date: datetime.date


class ShiftCreate(ShiftBase):
    pass


class Shift(ShiftBase):
    employeeId: uuid.UUID

    class Config:
        orm_mode = True


class ShiftGetPaginated(BaseModel):
    totalPages: int
    items: List[Shift]
##


# Products
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
