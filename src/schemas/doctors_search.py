from typing import Optional
from pydantic import BaseModel
from schemas import UserOut, UserDetailOut, DoctorQualificationOut
from schemas.doctor_chambers import DoctorChamberOut
from schemas.doctor_specialities import DoctorSpecialityOut


class DoctorSearchBase(BaseModel):
    User: UserOut
    UserDetail: UserDetailOut
    # DoctorQualification: DoctorQualificationOut


class DoctorSearchIn(BaseModel):
    name: Optional[str] = None
    speciality: Optional[str] = None


class DoctorSearchOut(BaseModel):
    User: UserOut
    DoctorSpeciality: DoctorSpecialityOut
    DoctorChamber: DoctorChamberOut

    class Config:
        orm_mode = True
