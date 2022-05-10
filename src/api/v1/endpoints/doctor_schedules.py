from fastapi import APIRouter
from exceptions.service_result import handle_result
from schemas import DoctorScheduleIn, DoctorScheduleOut
from db import get_db
from fastapi import Depends
from sqlalchemy.orm import Session
# from services import doctor_schedules_service



router = APIRouter()


# @router.post('/', response_model=DoctorScheduleOut)
# def create_schedule(schedule_in: DoctorScheduleIn, db: Session=Depends(get_db)):
#     schedule =  doctor_schedules_service.create(db=db, data_in=schedule_in)
#     return handle_result(schedule)



@router.get('/')
def all():
    return {'msg':'all schedule'}