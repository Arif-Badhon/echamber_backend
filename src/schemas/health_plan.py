from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel


class HealthPlanListBase(BaseModel):
    name: str
    details: str
    voucher_code: str
    total_patients: int
    expire_status: bool
    expire_date: Optional[date] = None
    days: Optional[int] = None
    fee: Optional[int] = None


class HealthPlanListIn(HealthPlanListBase):
    pass


class HealthPlanListUpdate(HealthPlanListBase):
    name: Optional[str] = None
    details: Optional[str] = None
    voucher_code: Optional[str] = None
    total_patients: Optional[int] = None
    expire_status: Optional[bool] = None
    expire_date: Optional[date] = None
    days: Optional[int] = None
    fee: Optional[int] = None


class HealthPlanListOut(HealthPlanListBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Health plan for patient

class HealthPlanForPatientBase(BaseModel):
    health_plan_id: int
    user_id: int
    register_by_id: int
    days: int
    fixed_amount: bool
    amount: int
    discount_percent: int


class HealthPlanForPatientIn(HealthPlanForPatientBase):
    pass


class HealthPlanForPatientWithoutHealthPlanId(BaseModel):
    user_id: int
    register_by_id: int
    discount_percent: int
    days: int
    fixed_amount: bool
    amount: int
    discount_percent: int


class HealthPlanForPatientUpdate(HealthPlanForPatientBase):
    health_plan_id: Optional[int] = None
    user_id: Optional[int] = None
    register_by_id: Optional[int] = None
    discount_percent: Optional[int] = None
    days: Optional[int] = None
    fixed_amount: Optional[bool] = None
    amount: Optional[int] = None
    discount_percent: Optional[int] = None


class HealthPlanForPatientOut(HealthPlanForPatientBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
