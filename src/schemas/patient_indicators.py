from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class PatientIndicatorBase(BaseModel):
    key: Optional[str] = None
    unit: Optional[str] = None
    slot_bool: Optional[bool] = None
    slot_int1: Optional[int] = None
    slot_int2: Optional[int] = None
    slot_int3: Optional[int] = None
    slot_str1: Optional[str] = None
    slot_str2: Optional[str] = None
    slot_str3: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True


class PatientIndicatorIn(PatientIndicatorBase):
    user_id: int


class PatientIndicatorUpdate(PatientIndicatorBase):
    pass


class PatientIndicatorOut(PatientIndicatorBase):
    user_id: Optional[int]
    created_at: datetime = None

    class Config:
        orm_mode = True
