from datetime import datetime
from typing import Optional
from pydantic import BaseModel

class HealthPartnerBase(BaseModel):
    name: str
    type: str
    district: str
    detail_address : str
    detail: str
    phone: str
    email: str
    contact_person: str
    contact_person_phone: str
    contact_person_email: str


class HealthPartnerIn(HealthPartnerBase):
    pass

class HealthPartnerUpdate(BaseModel):
    name: Optional[str] = None
    type: Optional[str] = None
    district: Optional[str] = None 
    detail_address : Optional[str] = None
    detail: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None
    contact_person: Optional[str] = None
    contact_person_phone: Optional[str] = None
    contact_person_email: Optional[str] = None



class HealthPartnerOut(HealthPartnerBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True