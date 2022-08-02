from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class DoctorWorkPlaceBase(BaseModel):
    institute: str
    position: str
    start_date: date
    end_date: Optional[date] = None


class DoctorWorkPlaceIn(DoctorWorkPlaceBase):
    pass


class DoctorWorkPlaceWithUser(DoctorWorkPlaceBase):
    user_id: int


class DoctorWorkPlaceUpdate(DoctorWorkPlaceBase):
    institute: Optional[str] = None
    position: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class DoctorWorkPlaceOut(DoctorWorkPlaceBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
