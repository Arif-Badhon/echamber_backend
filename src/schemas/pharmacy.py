from datetime import datetime
from pydantic import BaseModel
from typing import Optional
from .users import UserCreateWitoutRole

class PharmacyBase(BaseModel):
    name: str
    trade_lisence: str
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    drug_lisence: Optional[str] = None

class PharmacyIn(PharmacyBase):
    pass

class PharmacyUpdate(BaseModel):
    name: Optional[str] = None
    trade_lisence: Optional[str] = None
    detail_address: Optional[str] = None
    district: Optional[str] = None
    sub_district: Optional[str] = None
    drug_lisence: Optional[str] = None

class PharmacyOut(PharmacyBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PharmacyUserWithPharmacy(BaseModel):
    pharmacy: PharmacyIn
    user: UserCreateWitoutRole