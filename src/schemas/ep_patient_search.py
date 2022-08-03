from datetime import date
from typing import Optional
from pydantic import BaseModel

class EpPatientSearchOut(BaseModel):
    id: str
    name: str
    phone: str
    sex: str
    blood_group: Optional[str] = None
    dob: Optional[date] = None
    division: Optional[str] = None   

    class Config:
        orm_mode = True