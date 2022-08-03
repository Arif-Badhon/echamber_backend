from datetime import date, datetime
from pydantic import BaseModel
from typing import Optional


class EpNextFollowUpBase(BaseModel):
    date: date


class EpNextFollowUpIn(EpNextFollowUpBase):
    pass


class EpNextFollowUpWithEp(EpNextFollowUpBase):
    ep_id: int


class EpNextFollowUpUpdate(BaseModel):
    date: Optional[date] = None


class EpNextFollowUpOut(EpNextFollowUpBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
