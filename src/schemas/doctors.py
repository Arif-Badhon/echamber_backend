from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from pydantic.types import constr
from .image_log import ImageLogOut
from schemas.users import UserOut
from schemas.doctor_specialities import DoctorSpecialityOut
from schemas.doctor_qualifications import DoctorQualificationOut


class DoctorBase(BaseModel):
    user_id: int
    dr_title: Optional[str] = None
    bmdc: Optional[str] = None
    exp_year: Optional[int] = None
    online_fees: Optional[float] = None


class DoctorIn(DoctorBase):
    pass


class DoctorUpdate(BaseModel):
    dr_title: Optional[str] = None
    bmdc: Optional[str] = None
    exp_year: Optional[int] = None
    online_fees: Optional[float] = None


class DoctorOut(DoctorBase):
    id: int
    user_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class DoctorWithImages(DoctorBase):
    id: int
    user_id: int
    created_at: datetime
    images: List[ImageLogOut]

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
        min_length=11, max_length=14, regex=r"(^(\+88)?(01){1}[3-9]{1}\d{8})$"
    )
    sex: str
    password: str
    speciality: str
    qualification: str
    dr_title: Optional[str] = None
    bmdc: str
