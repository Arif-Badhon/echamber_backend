from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .users import UserCreateWitoutRole


class ClinicBase(BaseModel):
    name: str
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    clinic_is_active: bool= False


class ClinicIn(ClinicBase):
    pass


class ClinicUpdate(BaseModel):
    name:Optional[str] = None
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    clinic_is_active: bool= False


class ClinicOut(ClinicBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class ClinicUserWithClinic(BaseModel):
    clinic: ClinicIn
    user: UserCreateWitoutRole


class ClinicLogin(BaseModel):
    identifier: str
    password: str