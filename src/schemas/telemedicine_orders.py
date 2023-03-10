from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional
from schemas import ServiceOrderIn
from schemas.health_plan import HealthPlanListOut


class TelemedicineBase(BaseModel):
    health_plan_id: Optional[int] = None
    patient_id: Optional[int] = None
    doctor_id: Optional[int] = None
    schedule_id: Optional[int] = None
    booked_date: date


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


class TelemedicineServiceIn(BaseModel):
    service: ServiceOrderIn
    telemedicine: TelemedicineIn


class TelemedicineWithHealthplanOut(BaseModel):
    telemedicine: TelemedicineOut
    plan: HealthPlanListOut

    class Config:
        orm_mode = True