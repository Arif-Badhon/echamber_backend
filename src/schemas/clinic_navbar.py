from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ClinicNavbarBase(BaseModel):
    clinic_id: int
    nav_text: Optional[str] = None
    nav_href: Optional[str] = None


class ClinicNavbarIn(ClinicNavbarBase):
    pass


class ClinicNavbarUpdate(BaseModel):
    nav_text: Optional[str] = None
    nav_href: Optional[str] = None


class ClinicNavbarOut(ClinicNavbarBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
