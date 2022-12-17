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