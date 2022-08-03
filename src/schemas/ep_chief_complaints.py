from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Cc for chief complaints list

class CcBase(BaseModel):
    chief_complaints: str


class CcIn(CcBase):
    pass


class CcUpdate(CcBase):
    pass


class CcOut(BaseModel):
    id: int
    chief_complaints: str

    class Config:
        orm_mode = True


# Chief Complaints

class ChiefComplaintsBase(BaseModel):
    chief_complaints: str


class ChiefComplaintsIn(BaseModel):
    chief_complaints: str


class ChiefComplaintsWithEp(ChiefComplaintsBase):
    ep_id: int


class ChiefComplaintsUpdate(BaseModel):
    chief_complaints: Optional[str] = None


class ChiefComplaintsOut(ChiefComplaintsBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
