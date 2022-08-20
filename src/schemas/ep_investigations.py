from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# investigation list

class InvBase(BaseModel):
    investigation: str


class InvIn(InvBase):
    pass


class InvUpdate(InvBase):
    pass


class InvOut(InvBase):
    id: int
    investigation: str

    class Config:
        orm_mode = True


# Investigation

class EpInvestigationBase(BaseModel):
    investigation: str


class EpInvestigationIn(EpInvestigationBase):
    pass


class EpInvestigationWithEp(EpInvestigationBase):
    ep_id: int


class EpInvestigationUpdate(BaseModel):
    investigation: Optional[str] = None


class EpInvestigationOut(EpInvestigationBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
