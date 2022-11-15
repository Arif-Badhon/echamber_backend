from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .users import UserOut
from .user_details import UserDetailOut

class ClinicActivityBase(BaseModel):
    clinic_id: int
    user_id: int
    service_name: str
    service_received_id: int
    remark: str


class ClinicActivityIn(ClinicActivityBase):
    pass


class ClinicActivityUpdate(BaseModel):
    pass


class ClinicActivityOut(ClinicActivityBase):
    clinic_id: int
    user_id: int
    service_name: str
    service_received_id: int
    remark: str
    created_at: datetime = None


    class Config:
        orm_mode = True


class ClinicActivityAllOut(BaseModel):
    clinic_id: int
    user_id: int
    user_name: str
    user_phone: str
    service_name: str
    service_received_id: int
    remark: str
    created_at: datetime = None

    class Config:
        orm_mode = True


class ClinicActivityOutWithUser(BaseModel):
    ClinicActivity: ClinicActivityOut
    User: UserOut
    UserDetail: UserDetailOut