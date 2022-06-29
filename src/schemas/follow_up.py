from datetime import date, datetime
from typing import Literal, Optional
from pydantic import BaseModel

class FollowUpBase(BaseModel):
    # service_id: int
    status: Literal['pending', 'done']
    title: str
    remarks: str
    followup_date: date


class FollowUpIn(FollowUpBase):
    pass


class FollowUpInWithServiceId(FollowUpBase):
    service_id: int


class FollowUpUpdate(BaseModel):
    status: Literal['pending', 'done'] = None
    title: Optional[str] = None
    remarks: Optional[str] = None
    followup_date: Optional[date] = None


class FollowUpOut(FollowUpBase):
    id: int
    service_id: int
    status: str
    title: str
    remarks: str
    followup_date: date
    created_at: datetime

    class Config:
        orm_mode = True