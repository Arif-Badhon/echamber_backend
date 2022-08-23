from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class DoctorAcademicInfoBase(BaseModel):
    institute: str
    degree: str
    speciality: str
    start_date: date
    end_date: date


class DoctorAcademicInfoIn(DoctorAcademicInfoBase):
    pass


class DoctorAcademicInfoWithUser(DoctorAcademicInfoBase):
    user_id: int


class DoctorAcademicInfoUpdate(BaseModel):
    institute: Optional[str] = None
    degree: Optional[str] = None
    speciality: Optional[str] = None
    start_date: Optional[date] = None
    end_date: Optional[date] = None


class DoctorAcademicInfoOut(DoctorAcademicInfoBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
