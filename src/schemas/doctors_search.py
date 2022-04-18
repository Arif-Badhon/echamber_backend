from pydantic import BaseModel
from models.models import DoctorQualification
from schemas import UserOut, UserDetailOut, DoctorQualificationOut


class DoctorSearchBase(BaseModel):
    User: UserOut
    UserDetail: UserDetailOut
    # DoctorQualification: DoctorQualificationOut


class DoctorSearchOut(DoctorSearchBase):
    pass

    class Config:
        orm_mode = True
