from pydantic import BaseModel
from datetime import date
from typing import Optional


class TelemedicieBase(BaseModel):
    health_plan_id: Optional[int] = None
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    schedule_id: Optional[int] = None
    date: date


class TelemedicineIn(TelemedicieBase):
    pass


class TelemedicineInWithService(TelemedicieBase):
    service_id: int


class TelemedicineUpdate(BaseModel):
    health_plan_id: Optional[int] = None
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    schedule_id: Optional[int] = None
    date: Optional[date] = None


class TelemedicineOut(TelemedicieBase):
    id: int
    service_id: Optional[int] = None
    created_at: int

    class Config:
        orm_mode = True
