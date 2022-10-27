from pydantic import BaseModel
from datetime import datetime

class ClinicUserBase(BaseModel):
    user_id: int
    clinic_id: int


class ClinicUserIn(ClinicUserBase):
    pass


class ClinicUserWithClinicID(ClinicUserBase):
    clinic_id: int

    class Config:
        orm_mode = True


class ClinicUserUpdate(BaseModel):
    user_id: int

class ClinicUserHxId(BaseModel):
    your_clinic_hxclinicid: str

    class Config:
        orm_mode = True

class ClinicUserOut(ClinicUserBase):
    id: int
    user_id: int
    clinic_id: int
    created_at: datetime

    class Config:
        orm_mode = True