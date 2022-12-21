from pydantic import BaseModel
from enum import Enum
import enum
import datetime
import database
import uuid

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, Integer, String, Enum, Float, DateTime


class Menu(database.Base):
    __tablename__ = "menu"

    id = Column(UUID(as_uuid=True), primary_key=True,
                index=True, default=uuid.uuid4)
    restaurantId = Column(UUID(as_uuid=True), index=True, default=uuid.uuid4)
    name = Column(String)



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
