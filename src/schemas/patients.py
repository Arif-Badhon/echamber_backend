from datetime import date
from typing import Optional
from pydantic import BaseModel


class PatientBase(BaseModel):
    bio: Optional[str]
    marital_status: Optional[str]
    occupation: Optional[str]


class PatientIn(PatientBase):
    user_id: int


class PatientUpdate(PatientBase):
    pass


class PatientOut(PatientBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class PatientSignup(BaseModel):
    name: str
    email: str
    phone: str
    sex: str
    password: str
    country: str
    division: str
    district: str
    sub_district: str
    post_code: str
    dob: Optional[date] = None 


class PatientSignupOut(BaseModel):
    name: str
    email: str
    phone: str
    sex: str
    password: str
    country: str
    division: str
    district: str
    sub_district: str
    post_code: str
    dob: str

    class Config:
        orm_mode = True
