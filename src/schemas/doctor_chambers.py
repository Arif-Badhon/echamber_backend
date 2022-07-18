from typing import Optional
from pydantic import BaseModel


class DoctorChamberBase(BaseModel):
    name: str
    detail: str
    district: str
    detail_address: str


class DoctorChamberIn(DoctorChamberBase):
    user_id: int


class DoctorChamberUpdate(BaseModel):
    name: Optional[str] = None
    detail: Optional[str] = None
    district: Optional[str] = None
    detail_address: Optional[str] = None


class DoctorChamberOut(BaseModel):
    id: int
    user_id: int
    name: str
    detail: str
    district: str
    detail_address: str
    is_active: bool

    class Config:
        orm_mode = True
