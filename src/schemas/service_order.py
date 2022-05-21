from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class ServiceOrderBase(BaseModel):
    service_name: Optional[str] = None
    patient_id: Optional[int] = None
    order_placement: Optional[datetime] = None
    order_completion: Optional[datetime] = None
    order_value: Optional[int] = None
    discount_percent: Optional[int] = None
    payable_amount: Optional[int] = None
    payment_customer: Optional[int] = None
    payment_pending: Optional[int] = None
    payment_date: Optional[datetime] = None
    payment_method: Optional[str] = None
    payment_status: Optional[str] = None
    service_provider_type: Optional[str] = None
    service_provider_id: Optional[int] = None
    service_provider_fee: Optional[int] = None
    service_provider_fee_paid: Optional[int] = None
    service_provider_fee_pending: Optional[int] = None
    service_provider_fee_last_update: Optional[datetime] = None
    service_provider_fee_status: Optional[str] = None
    referral_type: Optional[str] = None
    referral_id: Optional[int] = None
    referral_provider_fee: Optional[int] = None
    referral_provider_fee_paid: Optional[int] = None
    referral_provider_fee_pending: Optional[int] = None
    referral_provider_fee_last_update: Optional[datetime] = None
    referral_provider_fee_status: Optional[str] = None
    current_address: Optional[str] = None
    remarks: Optional[str] = None

class ServiceOrderIn(ServiceOrderBase):
    pass 

class ServiceOrderUpdate(ServiceOrderBase):
    pass


class ServiceOrderOut(ServiceOrderBase):
    id: int
    created_at: date
    updated_at: Optional[date] = None

    class Config:
        orm_mode = True