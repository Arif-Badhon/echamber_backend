from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class TemporaryTokenBase(BaseModel):
    user_id: Optional[int] = None
    temp_token: Optional[str] = None
    used_status: Optional[bool] = None
    remarks: Optional[str] = None


class TemporaryTokenIn(TemporaryTokenBase):
    pass


class TemporaryTokenUpdate(TemporaryTokenBase):
    pass


class TemporaryTokenOut(TemporaryTokenBase):
    id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True
