from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class DoctorTrainingExpBase(BaseModel):
    topic: str
    place: str
    organisation: str
    year: int


class DoctorTrainingExpIn(DoctorTrainingExpBase):
    pass


class DoctorTrainingExpInWithUser(DoctorTrainingExpBase):
    user_id: int


class DoctorTrainingExpUpdate(BaseModel):
    topic: Optional[str] = None
    place: Optional[str] = None
    organisation: Optional[str] = None
    year: Optional[int] = None


class DoctorTrainingExpOut(DoctorTrainingExpBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
