from datetime import datetime
from typing import Literal, Optional
from pydantic import BaseModel


class DoctorEpHeaderBase(BaseModel):
    header_side: Literal['left', 'right']
    heading: str
    body: str


class DoctorEpHeaderIn(DoctorEpHeaderBase):
    user_id: int


class DoctorEpHeaderUpdate(BaseModel):
    header_side: Literal['left', 'right']
    heading: Optional[str] = None
    body: Optional[str] = None


class DoctorEpHeaderOut(DoctorEpHeaderBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True
