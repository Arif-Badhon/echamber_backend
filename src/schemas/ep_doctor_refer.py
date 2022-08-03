from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EpDoctorReferBase(BaseModel):
    detail: str


class EpDoctorReferIn(EpDoctorReferBase):
    pass


class EpDoctorReferWithEp(EpDoctorReferBase):
    ep_id: int


class EpDoctorReferUpdate(BaseModel):
    detail: Optional[str] = None


class EpDoctorReferOut(EpDoctorReferBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
