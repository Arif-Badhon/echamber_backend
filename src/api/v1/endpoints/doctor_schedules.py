from typing import List
from fastapi import APIRouter
from exceptions.service_result import handle_result
from schemas import DoctorScheduleBase, DoctorScheduleIn, DoctorScheduleOut, DoctorScheduleOutWithBooked, RangeScheduleInput, Msg
from db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
from services import doctor_schedule_service
from api.v1.auth_dependcies import logged_in_doctor, logged_in_employee
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


@router.get('/public/{doctor_user_id}', response_model=List[DoctorScheduleOut])
def get_all_schedule_public(doctor_user_id: int, date: date, db: Session = Depends(get_db)):
    all_ds = doctor_schedule_service.get_doctor_all_schedule(db=db, date=date, user_id=doctor_user_id)
    return handle_result(all_ds)


@router.patch('/booked_by_employee/{schedule_id}/{patient_id}', response_model=DoctorScheduleOut)
def booked_by_employee(schedule_id: int, patient_id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    booked = doctor_schedule_service.booked_by_employee(db=db, schedule_id=schedule_id, employee_id=current_user.id, patient_id=patient_id)
    return handle_result(booked)
