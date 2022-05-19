from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class ServiceOrderBase(BaseModel):
    service_name: str
    patient_id: int
    order_placement: datetime
    order_completion: datetime
    order_value: int
    discount_percent: int
    payable_amount: int
    payment_customer: int
    payment_pending: int
    payment_date: datetime
    payment_method: str
    service_provider_type: str
    service_provider_id: int
    service_provider_fee: int
    service_provider_fee_paid: int
    service_provider_fee_pending: int
    service_provider_fee_last_update: datetime
    service_provider_fee_status: str
    referral_type: str
    referral_id: int
    referral_provider_fee: int
    referral_provider_fee_paid: int
    referral_provider_fee_pending: int
    referral_provider_fee_last_update: datetime
    referral_provider_fee_status: str
    current_address: str
    remarks: str

class ServiceOrderIn(ServiceOrderBase):
    pass 

class ServiceOrderUpdate(BaseModel):
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


class ServiceOrderOut(ServiceOrderBase):
    id: int
    created_at: date
    updated_at: Optional[date] = None

    class Config:
        orm_mode = True