from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class EpDiagnosisBase(BaseModel):
    diagnosis_type: Optional[str] = None
    diagnosis: Optional[str] = None


class EpDiagnosisIn(EpDiagnosisBase):
    pass


class EpDiagnosisWithEp(EpDiagnosisBase):
    ep_id: int


class EpDiagnosisUpdate(BaseModel):
    diagnosis_type: Optional[str] = None
    diagnosis: Optional[str] = None


class EpDiagnosisOut(BaseModel):
    id: int
    ep_id: int
    diagnosis_type: Optional[str]
    diagnosis: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
