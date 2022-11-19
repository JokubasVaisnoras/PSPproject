from pydantic import BaseModel
from enum import Enum
import datetime


class TransactionType(Enum):
    cash = "cash"
    card = "card"


class Transaction(BaseModel):
    id: int
    emp_org_id: int
    cust_id: int
    order_id: int
    amount: int
    type: TransactionType
    created_timestamp: datetime.datetime


class DiscountType(str, Enum):
    percentage = "percentage"
    price = "price"


class Order(BaseModel):
    id: int
    cust_id: int
    tracking_code: int
    status: int
    note: str
    # we use datetime since it is equivalent to timestamp
    requested_timestamp: datetime.datetime
    estimated_timestamp: datetime.datetime


class Organization(BaseModel):
    id: int
    name: str
    credentials: dict
    settings: dict
    created_timestamp: int
    opening: int
    closing: int
    # Location added because it was not provided
    location: str


class Service(BaseModel):
    id: int
    org_id: int
    price: int
    description: str
    created_timestamp: int
    available: bool
    # Not provided:
    loyalty_point_reward: int


class EmployeeOrganization(BaseModel):
    id: int
    user_id: int
    org_id: int
    access: dict


class Shift(BaseModel):
    id: int
    emp_org_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    # Changing created_timestamp type from int to datetime
    created_timestamp: datetime.datetime


class OrderedService(BaseModel):
    id: int
    order_id: int
    service_id: int
    created_timestamp: int
    # Not provided:
    estimated_finish_time: datetime.datetime
    paid: bool


class Discount(BaseModel):
    id: int
    service_id: int
    percentage_off: int
    exact_price: int
    created_timestamp: datetime.datetime


class Coupon(Discount):
    coupon_id: int
    cust_id: int
    discount_id: int
    code: int
    created_timestamp: datetime.datetime
    valid_unit: datetime.datetime


class User(BaseModel):
    id: int
    password: str
    email: str
    full_name: str
    created_date: datetime.datetime
    phonenumber: str


class Employee(User):
    user_id: int
    org_id: int
    access: dict


class CensoredEmployee(Employee):
    password: None
