from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DoctorProfessionalMembershipBase(BaseModel):
    name: str
    position: str
    year: int


class DoctorProfessionalMembershipIn(DoctorProfessionalMembershipBase):
    pass


class DoctorProfessionalMembershipInWithUser(DoctorProfessionalMembershipBase):
    user_id: int


class DoctorProfessioanlMembershipUpdate(BaseModel):
    name: Optional[str] = None
    position: Optional[str] = None
    year: Optional[int] = None


class DoctorProfessionalMembershipOut(DoctorProfessionalMembershipBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
