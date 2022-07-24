from typing import Literal, Optional
from pydantic import BaseModel, constr, conint


class DoctorScheduleBase(BaseModel):
    day: Literal[1, 2, 3, 4, 5, 6, 7]
    hours: Literal[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    minutes: conint(gt=-1, lt=60)
    am_pm: Literal['am', 'pm']
    online: bool


class DoctorScheduleIn(DoctorScheduleBase):
    user_id: Optional[int] = None


class DoctorScheduleUpdate(DoctorScheduleBase):
    pass


class DoctorScheduleOut(DoctorScheduleBase):
    user_id: int

    class Config:
        orm_mode = True


class DoctorScheduleOutWithBooked(DoctorScheduleBase):
    user_id: int
    booked: bool

    class Config:
        orm_mode = True
