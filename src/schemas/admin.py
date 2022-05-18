from datetime import datetime
from pydantic import BaseModel
from .doctors import DoctorOut
from .users import UserOut
from .doctor_qualifications import DoctorQualificationOut
from .doctor_specialities import DoctorSpecialityOut

class UserDoctorOut(BaseModel):
    User: UserOut
    Doctor: DoctorOut
    DoctorQualification: DoctorQualificationOut
    DoctorSpeciality: DoctorSpecialityOut

    class Config:
        orm_mode = True



class AdminPanelActivityBase(BaseModel):
    user_id: int
    service_name: str
    service_recived_id: int
    remark: str

class AdminPanelActivityIn(AdminPanelActivityBase):
    pass

class AdminPanelActivityUpdate(AdminPanelActivityBase):
    pass

class AdminPanelActivityOut(BaseModel):
    user_id: int
    service_name: str
    service_recived_id: int
    remark: str
    created_at: datetime = None

    class Config:
        orm_mode = True


class AdminPanelActivityAllOut(BaseModel):
    user_id: int
    user_name: str
    user_phone: str
    service_name: str
    service_recived_id: int
    remark: str
    created_at: datetime = None

    class Config:
        orm_mode = True

class ResultInt(BaseModel):
    results: int

    class Config:
        orm_mode = True