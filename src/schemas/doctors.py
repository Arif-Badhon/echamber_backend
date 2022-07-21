from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.types import constr

from schemas.users import UserOut
from schemas.doctor_specialities import DoctorSpecialityOut
from schemas.doctor_qualifications import DoctorQualificationOut


class DoctorBase(BaseModel):
    user_id: int
    bmdc: Optional[str] = None
    exp_year: Optional[int] = None
    online_fees: Optional[float]


class DoctorIn(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    bmdc: Optional[str] = None
    exp_year: Optional[int] = None
    online_fees: Optional[float]


class DoctorOut(DoctorBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class DoctorDetails(BaseModel):
    user: UserOut
    doctor: DoctorOut
    specialities: List[DoctorSpecialityOut]
    qualifications: List[DoctorQualificationOut]


class DoctorUserWithSpecialities(BaseModel):
    id: int
    name: str
    sex: str
    specialities: List[DoctorSpecialityOut]

    class Config:
        orm_mode = True


class DoctorSignup(BaseModel):
    name: str
    email: str
    phone: constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )
    sex: str
    password: str
    speciality: str
    qualification: str
    bmdc: str
