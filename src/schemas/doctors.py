from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr


class DoctorBase(BaseModel):
    user_id: int
    bmdc: Optional[str] = None
    main_chamber: Optional[str] = None


class DoctorIn(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    bmdc: Optional[str]
    left_header: Optional[str]
    right_header: Optional[str]


class DoctorOut(DoctorBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True


class DoctorSignup(BaseModel):
    name: str
    email: str
    phone: constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )
    sex: str
    password: str
    speciality: str
    qualification: str
    bmdc: str
