from typing import Optional
from pydantic import BaseModel


class DoctorSpecialityIn(BaseModel):
    user_id: int
    speciality: str


class DoctorSpecialityUpdate(BaseModel):
    user_id: Optional[int] = None
    speciality: Optional[str] = None


class DoctorSpecialityOut(BaseModel):
    id: int
    user_id: int
    speciality: str

    class Config:
        orm_mode = True
