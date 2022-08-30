from typing import Optional
from pydantic import BaseModel


class DoctorChamberBase(BaseModel):
    name: str
    detail: str
    district: str
    detail_address: Optional[str] = None
    chamber_fee: Optional[int] = None


class DoctorChamberIn(DoctorChamberBase):
    user_id: int


class DoctorChamberUpdate(BaseModel):
    name: Optional[str] = None
    detail: Optional[str] = None
    district: Optional[str] = None
    detail_address: Optional[str] = None
    chamber_fee: Optional[int] = None


class DoctorChamberOut(DoctorChamberBase):
    id: int
    user_id: int
    is_active: bool

    class Config:
        orm_mode = True
