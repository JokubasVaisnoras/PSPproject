from enum import Enum
import enum
import database
import uuid
import enum
import schema

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Enum, Float, DateTime, Date


class Menu(database.Base):
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    restaurantId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    name = Column(String)


<<<<<<< HEAD
class EmployeePositionEnum(enum.StrEnum):
    Waiter = "Waiter"
    Chef = "Chef"
    Administrator = "Administrator"


class Employee(database.Base):
    __tablename__ = "employee"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    name = Column(String)
    lastName = Column(String)
    loginCode = Column(String)
    position = Column(Enum(EmployeePositionEnum))
    scheduleId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    salary = Column(Integer)
    tipsAmount = Column(Integer)


class Shift(database.Base):
    __tablename__ = "shift"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    employeeId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    startTime = Column(DateTime(timezone=True))
    endTime = Column(DateTime(timezone=True))
    date = Column(Date)

 
class Order_Item(database.Base):
    __tablename__ = "order_item"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    orderId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    menuItem = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    quantity = Column(Integer)
    status = Column(Enum(schema.OrderItemStatusEnum))
    comment = Column(String)
    startDate = Column(DateTime(timezone=True))
    endDate = Column(DateTime(timezone=True))


class MenuItem(database.Base):
    __tablename__ = "menu_item"
    
    id = Column(UUID(as_uuid=True), primary_key=True,
            index=True, default=uuid.uuid4)
    recipeId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    description = Column(String)
    photo = Column(String)
    cookingDescription = Column(String)
    state = Column(Enum(schema.MenuItemStateEnum))
    defaultDiscount = Column(Float)
    loyaltyDiscount = Column(Float)
    price = Column(Float)


class MeasuringTypeEnum(enum.StrEnum):
    kg = "kg"
    g = "g"
    l = "l"
    ml = "ml"
    unit = "unit"


class Product(database.Base):
    __tablename__ = "product"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    name = Column(String)
    restaurantId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    measuringType = Column(Enum(MeasuringTypeEnum))
    amount = Column(Integer)
    price = Column(Float)


class Payment(database.Base):
    __tablename__ = "payments"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    orderId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    price = Column(Float)
    taxAmount = Column(Float)
    tips = Column(Float)
    cardId = Column(String)
    paymentType = Column(String)
    paymentDate = Column(DateTime(timezone=True))


class Recipe(database.Base):
    __tablename__ = "recipes"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    productId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    menuItemId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    amount = Column(Float)
    measuringType = Column(Enum(MeasuringTypeEnum))
