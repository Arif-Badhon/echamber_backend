from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional


class TelemedicineBase(BaseModel):
    health_plan_id: Optional[int] = None
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    schedule_id: Optional[int] = None
    date: Optional[date] = None


class TelemedicineIn(TelemedicineBase):
    pass


class TelemedicineInWithService(TelemedicineBase):
    service_order_id: int


class TelemedicineUpdate(TelemedicineBase):
    pass


class TelemedicineOut(TelemedicineBase):
    id: int
    service_order_id: Optional[int] = None
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True
