from fastapi import Body, FastAPI
from pydantic import BaseModel
import datetime

app = FastAPI()

tags_metadata = [
    {
        "name": "services",
        "description": "Operations with services.",
    },
]

tags_metadata = [
    {
        "name": "manage_staff",
        "description": "Operations with staff management.",
    },
]

tags_metadata = [
    {
        "name": "manage_organizations",
        "description": "Operations with organization management.",
    },
]

tags_metadata = [
    {
        "name": "manage_shifts",
        "description": "Operations with shift management.",
    },
]


class Organization(BaseModel):
    id: int
    name: str
    credentials: dict
    settings: dict
    created_timestamp: int
    opening: int
    closing: int
    #Location added because it was not provided
    location: str


class Service(BaseModel):
    id: int
    org_id: int
    price: int
    description: str
    created_timestamp: int
    available: bool

class EmployeeOrganizations(BaseModel):
    id: int
    user_id:int
    org_id: int
    access: dict

class Shifts(BaseModel):
    id: int
    emp_org_id: int
    start_time: datetime.datetime
    end_time: datetime.datetime
    #Changing created_timestamp type from int to datetime
    created_timestamp: datetime.datetime

class OrderedService(BaseModel):
    id: int
    order_id: int
    service_id: int
    created_timestamp: int

class Discount(BaseModel):
    id:int
    service_id:int
    percentage_off:int
    exact_price:int
    created_timestamp:datetime.datetime

class User(BaseModel):
    id: int
    password: str
    email: str
    full_name: str
    created_date: datetime.datetime
    phonenumber: str
    

@app.get("/organizations/{organization_id}/services/search", tags=["services"], response_model=list[Service])
async def search_services(name: str) -> list[Service]:
    return None


@app.put("/organizations/{organization_id}/services/{service_id}/reserve", tags=["services"], response_model=OrderedService)
async def reserve_service() -> OrderedService:
    return None


@app.put("/organizations/{organization_id}/reservations/{reservation_id}/handle", tags=["services"], response_model=OrderedService)
async def handle_reservation() -> OrderedService:
    return None


@app.post("/organizations/{organization_id}/reservations/{reservation_id}/addnote", tags=["services"], response_model=OrderedService)
async def reservation_add_note(note: str = Body()) -> OrderedService:
    return None


@app.post("/organizations/{organization_id}/services/add", tags=["services"], response_model=Service)
async def add_service() -> Service:
    return None


@app.delete("/organizations/{organization_id}/services/{service_id}/remove", tags=["services"])
async def remove_service(organization_id:int,service_id:int) -> None:
    return "succesful"


@app.put("/organizations/{organization_id}/services/{service_id}/discounts", tags=["services"],response_model=Discount)
async def remove_service(organization_id:int,service_id:int) -> Discount:
    return None

@app.post("/customers/user/add", tags=["Customer"],response_model=User)
async def create_account() -> User:
    return None

@app.get("/customers/{customer_id}/info", tags=["Customer"],response_model=User)
async def check_information(customer_id:int) -> User:
    return None

@app.put("/customers/{customer_id}/info", tags=["Customer"],response_model=User)
async def update_information(customer_id:int) -> User:
    return None

@app.post("/organizations/{organization_id}/add_location", tags=["manage_organizations"], response_model=Organization)
async def organization_add_location(note: str = Body({"location":"Test street 1"})) -> Organization:
    return None

@app.post("/organizations/{organization_id}/add_bank_credentials", tags=["manage_organizations"], response_model=Organization)
async def organization_add_bank_data(note: str = Body({"account_number":"LT0000000000000222"})) -> Organization:
    return None

@app.post("/organizations/{organization_id}/add_working_hours", tags=["manage_organizations"], response_model=Organization)
async def organization_add_opening_time(note: str = Body({"opening":10,"closing":22})) -> Organization:
    return None

@app.delete("/organizations/{organization_id}", tags=["manage_organizations"])
async def delete_response():
    return None

@app.post("/organizations/{organization_id}/employees", tags=["manage_staff"], response_model=EmployeeOrganizations)
async def staff_add_employee(note: str = Body({"id":1, "user_id": 15, "org_id": 1337, "access":{"access1":True,"access2":False}})) -> Organization:
    return None

@app.delete("/organizations/{organization_id}/employees/{user_id}", tags=["manage_staff"])
async def delete_response():
    return None

@app.post("/organizations/{organization_id}/shifts", tags=["manage_shifts"], response_model=Shifts)
async def shifts_add_shift(note: str = Body({"id":1, "emp_org_id": 55, "start_time": "2008-09-15T15:53:00+05:00", "end_time":"2008-10-15T15:53:00+05:00", "created_timestamp":"2007-09-15T15:53:00+05:00"})) -> Organization:
    return None

@app.put("/organizations/{organization_id}/shifts/{shift_id}", tags=["manage_shifts"], response_model=Shifts)
async def shifts_edit_shift_information(note:str = Body({"id":0, "emp_org_id":0})) -> Shifts:
    return None
