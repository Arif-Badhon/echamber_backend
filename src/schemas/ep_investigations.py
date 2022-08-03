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

class InvestigationBase(BaseModel):
    investigation: str


class InvestigationIn(InvestigationBase):
    pass


class InvestigationWithEp(InvestigationBase):
    ep_id: int


class InvestigationUpdate(BaseModel):
    investigation: Optional[str] = None


class InvestigationOut(InvestigationBase):
    id: int
    ep_id: int
    created_at: datetime
