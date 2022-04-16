from typing import Optional
from pydantic import BaseModel


class DoctorChamberBase(BaseModel):
    name: str
    detail: str


class DoctorChamberIn(DoctorChamberBase):
    user_id: int


class DoctorChamberUpdate(BaseModel):
    name: Optional[str] = None
    detail: Optional[str] = None


class DoctorChamberOut(BaseModel):
    id: int
    user_id: int
    name: str
    detail: str
    is_active: bool

    class Config:
        orm_mode = True
