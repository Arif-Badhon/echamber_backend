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
    slot_flt4: Optional[float] = None
    slot_flt5: Optional[float] = None
    slot_flt6: Optional[float] = None
    slot_str7: Optional[str] = None
    slot_str8: Optional[str] = None
    slot_str9: Optional[str] = None

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
