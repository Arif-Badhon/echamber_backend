from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class CorporatePartnerBase(BaseModel):
    name: str
    type: str
    district: str
    detail_address: str
    detail: str
    phone: str
    email: str
    contact_person: str
    contact_person_phone: str
    contact_person_email: str

class CorporatePartnerIn(CorporatePartnerBase):
    pass

class CorporatePartnerUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    district: Optional[str] = None
    detail_address: Optional[str] = None
    detail: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    contact_person: Optional[str] = None
    contact_person_phone: Optional[str] = None
    contact_person_email: Optional[str] = None

class CorporatePartnerOut(CorporatePartnerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True



class CorporatePartnerUserBase(BaseModel):
    corporate_id: int
    users_id: int
    department: Optional[str] = None

class CorporatePartnerUserIn(CorporatePartnerUserBase):
    pass

class CorporatePartnerUserUpdate(BaseModel):
    corporate_id: Optional[int] = None
    users_id: Optional[int] = None
    department: Optional[str] = None

class CorporatePartnerUserOut(CorporatePartnerUserBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True