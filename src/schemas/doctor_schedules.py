from typing import Literal, Optional, List
from pydantic import BaseModel, constr, conint
from datetime import date


class DoctorScheduleBase(BaseModel):
    date: date
    time_min: conint(gt=-1, lt=1441)
    am_pm: Literal['am', 'pm']
    online: bool
    chamber_id: Optional[int] = None
    booked_by_patient_id: Optional[int] = None
    duration_min: conint(gt=-1, lt=1441)


class DoctorScheduleIn(DoctorScheduleBase):
    user_id: Optional[int] = None


class DoctorScheduleUpdate(DoctorScheduleBase):
    pass


class DoctorScheduleOut(DoctorScheduleBase):
    user_id: int
    time: Optional[str] = None

    class Config:
        orm_mode = True


class DoctorScheduleOutWithBooked(DoctorScheduleBase):
    user_id: int
    booked: bool

    class Config:
        orm_mode = True


# Range Scheduele input

class RangeScheduleInput(BaseModel):
    date_start: date
    date_end: date
    time_start: str = "12:00"
    time_end: str = "12:10"
    time_start_am_pm: Literal['am', 'pm']
    time_end_am_pm: Literal['am', 'pm']
    week_day: List[Literal['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']]
    online: bool
    chamber_id: Optional[int] = None
    booked_by_patient_id: Optional[int] = None
    duration_min: conint(gt=0, lt=1441)
