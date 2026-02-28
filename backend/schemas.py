# schemas.py
from pydantic import BaseModel, EmailStr
from datetime import date

class UserCreate(BaseModel):
    name: str
    email: EmailStr
    password: str

class UserLogin(BaseModel):
    email: EmailStr
    password: str


class OutletCreate(BaseModel):
    name: str
    address: str
    city: str


class VisitCreate(BaseModel):
    outlet_id: int
    notes: str
    cases_sold: int
    date: str


class VisitCreate(BaseModel):
    outlet_id: int
    notes: str
    cases_sold: int
    date: date