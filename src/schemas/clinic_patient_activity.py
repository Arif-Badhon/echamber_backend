from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ClinicPatientActivityBase(BaseModel):
    clinic_id: int
    patient_id: int
    service_name: Optional[str] = None
    service_received_id: Optional[int] = None
    remark: Optional[str] = None


class ClinicPatientActivityIn(ClinicPatientActivityBase):
    pass


class ClinicPatientActivityUpdate(BaseModel):
    service_name: Optional[str] = None
    service_received_id: Optional[int] = None
    remark: Optional[str] = None


class ClinicPatientActivityOut(ClinicPatientActivityBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True