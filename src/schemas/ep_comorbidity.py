from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EpCoMorbidityBase(BaseModel):
    cm_type: Optional[str] = None
    remarks: Optional[str] = None


class EpCoMorbidityIn(EpCoMorbidityBase):
    pass


class EpCoMorbidityWithEp(EpCoMorbidityBase):
    ep_id: int


class EpCoMorbidityUpdate(BaseModel):
    cm_type: Optional[str] = None
    remarks: Optional[str] = None


class EpCoMorbidityOut(EpCoMorbidityBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
