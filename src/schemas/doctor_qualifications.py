from pydantic import BaseModel
from typing import Optional


class DoctorQualilficationIn(BaseModel):
    user_id: int
    qualification: str


class DoctorQualilficationUpdate(BaseModel):
    qualification: Optional[str] = None


class DoctorQualificationOut(BaseModel):
    id: int
    user_id: int
    qualification: str

    class Config:
        orm_mode = True