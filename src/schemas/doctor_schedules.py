from pydantic import BaseModel

class DoctorScheduleBase(BaseModel):
    doctor_id: int
    patient_id:int
    chamber_id: int
    date: str
    time: str
    payable_amount: int
    payment: int
    pending: int
    others: str = None


class DoctorScheduleIn(DoctorScheduleBase):
    pass


class DoctorScheduleUpdate(BaseModel):
    doctor_id: int = None
    patient_id:int = None
    chamber_id: int = None
    date: str = None
    time: str = None
    payable_amount: int = None
    payment: int = None
    pending: int = None
    others: str = None

class DoctorScheduleOut(DoctorScheduleBase):
    pass

    class Config:
        orm_mode = True

