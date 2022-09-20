from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from .users import UserCreateWitoutRole


class PharmacyBase(BaseModel):
    name: str
    trade_license: str
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    drug_license: Optional[str] = None
    pharmacy_is_active: bool = False


class PharmacyIn(PharmacyBase):
    pass


class PharmacyUpdate(BaseModel):
    name: Optional[str] = None
    trade_license: Optional[str] = None
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    drug_license: Optional[str] = None
    pharmacy_is_active: Optional[bool] = None


class PharmacyOut(PharmacyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PharmacyUserWithPharmacy(BaseModel):
    pharmacy: PharmacyIn
    user: UserCreateWitoutRole


# login schema

class PharmacyLogin(BaseModel):
    trade_license: str
    identifier: str
    password: str
