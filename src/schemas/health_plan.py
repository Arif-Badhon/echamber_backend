from datetime import date, datetime
from typing import Optional
from pydantic import BaseModel
from .service_order import ServiceOrderIn


class HealthPlanListBase(BaseModel):
    plan_type: Optional[str] = None
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


class HealthPlanListUpdate(BaseModel):
    plan_type: Optional[str] = None
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
    service_order_id: int


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
    service_order_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class HealthPlanForPatientWithService(BaseModel):
    service: ServiceOrderIn
    health_plan_subscribe: HealthPlanForPatientWithoutHealthPlanId
