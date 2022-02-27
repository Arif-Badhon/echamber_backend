from typing import Optional
from pydantic import BaseModel


class DoctorBase(BaseModel):
    bmdc: str
    left_header: Optional[str]
    right_header: Optional[str]


class DoctorIn(DoctorBase):
    user_id: int


class DoctorUpdate(BaseModel):
    bmdc: Optional[str]
    left_header: Optional[str]
    right_header: Optional[str]


class DoctorOut(DoctorBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
