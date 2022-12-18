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


# class OrderItemWithId(BaseModel):


