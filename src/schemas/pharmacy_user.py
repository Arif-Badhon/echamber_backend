from datetime import datetime
from pydantic import BaseModel

class PharmacyUserBase(BaseModel):
    user_id: int
    pharmacy_id: int

class PharmacyUserIn(PharmacyUserBase):
    pass

class PharmacyUserWithPharmacyID(PharmacyUserBase):
    pharmacy_id: int

    class Config:
        orm_mode = True

class PharmacyUserUpdate(BaseModel):
    user_id: int

class PharmacyUserHxId(BaseModel):
    your_pharmacy_hxpharmacyid: str

    class Config:
        orm_mode = True

class PharmacyUserOut(PharmacyUserBase):
    id: int
    user_id: int
    pharmacy_id: int
    created_at: datetime

    class Config:
        orm_mode = True