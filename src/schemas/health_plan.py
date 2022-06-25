from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class HealthPlanListBase(BaseModel):
    name: str
    details: str
    voucher_code: str
    total_patients: int
    expire_status: bool
    expire_date: date


class HealthPlanListIn(HealthPlanListBase):
    pass

class HealthPlanListUpdate(HealthPlanListBase):
    name: Optional[str] = None
    details: Optional[str] = None
    voucher_code: Optional[str] = None
    total_patients: Optional[int] = None
    expire_status: Optional[bool] = None
    expire_date: Optional[date] = None


class HealthPlanListOut(HealthPlanListBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Health plan for patient

class HealthPlanForPatientBase(BaseModel):
    health_plan_id: int
    user_id: int
    register_by: int
    discount_percent: int
    days: int

class HealthPlanForPatientIn(HealthPlanForPatientBase):
    pass

class HealthPlanForPatientUpdate(HealthPlanForPatientBase):
    health_plan_id: Optional[int] = None
    user_id: Optional[int] = None
    register_by: Optional[int] = None
    discount_percent: Optional[int] = None
    days: Optional[int] = None

class HealthPlanFroPatientOut(HealthPlanForPatientBase):
    id: int 
    created_at: datetime

    class Config:
        orm_mode = True