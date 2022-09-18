from typing import List
from fastapi import APIRouter
from exceptions.service_result import handle_result
from schemas import DoctorScheduleBase, DoctorScheduleIn, DoctorScheduleOut, DoctorScheduleOutWithBooked, RangeScheduleInput, Msg
from db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from services import doctor_schedule_service
from api.v1.auth_dependcies import logged_in_doctor
from datetime import date

router = APIRouter()


@router.get('/', response_model=List[DoctorScheduleOut])
def get_all_schedule(date: date, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    all_ds = doctor_schedule_service.get_doctor_all_schedule(db=db, date=date, user_id=current_user.id)
    return handle_result(all_ds)


@router.post('/range/', response_model=Msg)
def range_input(data_in: RangeScheduleInput, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    ds = doctor_schedule_service.submit_with_range(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(ds)


# @router.get('/', response_model=List[DoctorScheduleOut])
# def schedules(db: Session = Depends(get_db), current_doctor: Session = Depends(logged_in_doctor)):
#     all_schedule = doctor_schedule_service.get_by_key(db=db, skip=0, limit=1440, descending=False, count_results=False, user_id=current_doctor.id)
#     return handle_result(all_schedule)


# @router.post('/', response_model=DoctorScheduleOut)
# def create_schedule(data_in: DoctorScheduleBase, db: Session = Depends(get_db), current_doctor: Session = Depends(logged_in_doctor)):
#     schedule = doctor_schedule_service.create(db=db, data_in=DoctorScheduleIn(user_id=current_doctor.id, **data_in.dict()))
#     return handle_result(schedule)


# @router.get('/booked/{doctor_id}/{date}', response_model=List[DoctorScheduleOutWithBooked])
# def booked_schedule(doctor_id: int, date: date, db: Session = Depends(get_db)):
#     data = doctor_schedule_service.booked_schedule(db=db, doctor_id=doctor_id, date=date)
#     return handle_result(data)
