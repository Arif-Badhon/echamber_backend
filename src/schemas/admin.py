from datetime import datetime
from pydantic import BaseModel
from .doctors import DoctorOut
from .users import UserOut
from .doctor_qualifications import DoctorQualificationOut
from .doctor_specialities import DoctorSpecialityOut
from typing import Optional


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



class AdminPatientsOut(BaseModel):
    id: int
    name: str
    email: Optional[str] = None
    phone: str
    sex: str
    is_active: bool
    created_at: datetime
    register_by_id: Optional[int] = None 
    register_by_name: Optional[str] = None
    register_by_role: Optional[str] = None
    company_name: Optional[str] = None

    class Config:
        orm_mode = True