from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PatientFamilyBase(BaseModel):
    user_id: Optional[int] = None
    relation_with: Optional[int] = None
    relation_from: Optional[str] = None
    relation_to: Optional[str] = None
    relationship_status: Optional[str] = None
    message: Optional[str] = None


class PatientFamilyIn(PatientFamilyBase):
    pass

class PatientFamilyReuest(BaseModel):
    relation_with: int
    relation_from: str
    relation_to: str
    message: Optional[str] = None

class PatientFamilyUpdate(PatientFamilyBase):
    relation_with: Optional[int] = None
    relation_from: Optional[str] = None
    relation_to: Optional[str] = None
    relationship_status: Optional[str] = None
    message: Optional[str] = None
    

class PatientFamilyOut(PatientFamilyBase):
    id: int 
    created_at: datetime

    class Config:
        orm_mode = True