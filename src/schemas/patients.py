from typing import Optional
from pydantic import BaseModel


class PatientBase(BaseModel):
    bio: Optional[str]
    nid: Optional[str]
    marital_status: Optional[str]
    occupation: Optional[str]


class PatientIn(PatientBase):
    user_id: int


class PatientUpdate(PatientBase):
    pass


class PatientOut(PatientBase):
    id: int
    user_id: int
