from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EpOnExaminationBase(BaseModel):
    ep_id: int
    patient_indicator_id: int


class EpOnExaminationIn(EpOnExaminationBase):
    pass


class EpOnExaminationUpdate(BaseModel):
    ep_id: Optional[int] = None
    patient_indicator_id: Optional[int] = None


class EpOnExaminationOut(EpOnExaminationBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
