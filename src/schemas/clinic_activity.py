from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ClinicActivityBase(BaseModel):
    user_id: int
    service_name: str
    service_received_id: int
    remark: str


class ClinicActivityIn(ClinicActivityBase):
    pass


class ClinicActivityUpdate(BaseModel):
    pass


class ClinicActivityOut(ClinicActivityBase):
    user_id: int
    service_name: str
    service_recived_id: int
    remark: str
    created_at: datetime = None


    class Config:
        orm_mode = True


class ClinicActivityAllOut(BaseModel):
    user_id: int
    user_name: str
    user_phone: str
    service_name: str
    service_recived_id: int
    remark: str
    created_at: datetime = None

    class Config:
        orm_mode = True