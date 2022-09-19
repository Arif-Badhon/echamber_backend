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


@router.post('/range/', response_model=Msg, description='weekday = mon, tue, wed, thu, fri, sat, sun')
def range_input(data_in: RangeScheduleInput, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    ds = doctor_schedule_service.submit_with_range(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(ds)
