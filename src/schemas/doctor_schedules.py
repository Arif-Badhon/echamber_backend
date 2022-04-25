from pydantic import BaseModel


class DoctorScheduleIn(BaseModel):
    date: str
    time: int 
    others: str = None

class DoctorScheduleOut():
    date: str
    time: int
    others: str = None

    class Config:
        orm_mode = True

