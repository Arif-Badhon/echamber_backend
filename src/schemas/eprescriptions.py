from datetime import datetime
from pydantic import BaseModel
from typing import Optional


###############
#   Ep base   #
###############


class EpBase(BaseModel):
    cause_of_consultation: Optional[str] = None
    telemedicine_order_id: Optional[int] = None
    doctor_id: int
    patient_id: int
    age: int
    current_address: Optional[str] = None
    remarks: Optional[str] = None


class EpIn(EpBase):
    pass


class EpUpdate(BaseModel):
    cause_of_consultation: Optional[str] = None
    telemedicine_order_id: Optional[int] = None
    doctor_id: Optional[int] = None
    patient_id: Optional[int] = None
    age: Optional[int] = None
    current_address: Optional[str] = None
    remarks: Optional[str] = None


class EpOut(EpBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
