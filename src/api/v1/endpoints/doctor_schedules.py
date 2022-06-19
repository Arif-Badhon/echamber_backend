from typing import List
from fastapi import APIRouter
from exceptions.service_result import handle_result
from schemas import DoctorScheduleBase, DoctorScheduleIn, DoctorScheduleOut
from db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from services import doctor_schedule_service
from api.v1.auth_dependcies import logged_in_doctor


router = APIRouter()


@router.get('/', response_model=List[DoctorScheduleOut])
def schedules(db: Session = Depends(get_db), current_doctor: Session = Depends(logged_in_doctor)):
    all_schedule = doctor_schedule_service.get_by_key(db=db, skip=0, limit=1440, descending=False, count_results=False, user_id=current_doctor.id)
    return handle_result(all_schedule)


@router.post('/', response_model=DoctorScheduleOut)
def create_schedule(data_in: DoctorScheduleBase, db: Session = Depends(get_db), current_doctor: Session = Depends(logged_in_doctor)):
    schedule = doctor_schedule_service.create(db=db, data_in=DoctorScheduleIn(user_id=current_doctor.id, **data_in.dict()))
    return handle_result(schedule)