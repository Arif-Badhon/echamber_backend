from pydantic import BaseModel
from datetime import datetime
from .users import UserOut


class ClinicWithDoctorBase(BaseModel):
    clinic_id: int
    doctor_id: int


class ClinicWithDoctorIn(ClinicWithDoctorBase):
    pass


class ClinicWithDoctorUpdate(BaseModel):
    pass


class ClinicWithDoctorOut(ClinicWithDoctorBase):
    id: int
    created_at: datetime
    clinic_id: int
    doctor_id: int

    class Config:
        orm_mode = True



class ClinicWithDoctorDetails(BaseModel):
    ClinicWithDoctor: ClinicWithDoctorOut
    User: UserOut