from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class HistoryBase(BaseModel):
    history_type: str
    history: str


class HistoryIn(HistoryBase):
    pass


class HistoryWithEp(HistoryBase):
    ep_id: int


class HistoryUpdate(BaseModel):
    history_type: Optional[str] = None
    history: Optional[str] = None


class HistoryOut(BaseModel):
    id: int
    ep_id: int
    created_at: datetime
