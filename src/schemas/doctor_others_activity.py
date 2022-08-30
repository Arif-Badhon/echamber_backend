from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DoctorOthersAcivityBase(BaseModel):
    topic: Optional[str] = None
    title: Optional[str] = None
    details: Optional[str] = None


class DoctorOthersActivityIn(DoctorOthersAcivityBase):
    pass


class DoctorOthersActivityWithUser(DoctorOthersAcivityBase):
    user_id: int


class DoctorOthersActivityUpdate(BaseModel):
    topic: Optional[str] = None
    title: Optional[str] = None
    details: Optional[str] = None


class DoctorOthersActivityOut(DoctorOthersAcivityBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
