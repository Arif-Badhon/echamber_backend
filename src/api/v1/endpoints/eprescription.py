from typing import List, Union
from fastapi import APIRouter
from db import get_db
from exceptions.service_result import handle_result
from schemas.eprescriptions import EpIn, EpAllOut, EpOut
from services import patients_service, ep_service, doctor_ep_header_service
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas import EpPatientSearchOut, EpOut, EpOutWithDoctorName, EpAllOut, EpDiagnosisOut, DoctorEpHeaderOut, DoctorEpHeaderUpdate, ResultInt
from api.v1.auth_dependcies import logged_in, logged_in_doctor, logged_in_employee, logged_in_moderator, logged_in_patient
from utils import beginning_date, current_date

router = APIRouter()


@router.get('/patient-search', response_model=List[EpPatientSearchOut])
def patient_search_by_name(name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    patients = patients_service.search_by_patient_name(db=db, name=name, skip=skip, limit=limit)
    return handle_result(patients)


@router.get('/doctor-ep-header/{doctor_id}', response_model=List[DoctorEpHeaderOut])
def doctor_ep_header_by_user(doctor_id: int, db: Session = Depends(get_db)):
    header = doctor_ep_header_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, user_id=doctor_id)
    return handle_result(header)

# , response_model=List[DoctorEpHeaderOut]


@router.patch('/doctor-ep-header/{user_id}')
def doctor_ep_header_update(data_in: DoctorEpHeaderUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    up = doctor_ep_header_service.update_or_create(db=db, user_id=current_user.id, data_in=data_in)
    return handle_result(up)


@router.post('/', response_model=EpOut)
def submit(data_in: EpIn, db: Session = Depends(get_db)):
    e = ep_service.submit(data_in=data_in, db=db)
    return e


# @router.get('/{id}')
# , response_model=EpAllOut
@router.get('/{id}', response_model=EpAllOut)
def single_prescription(id: int, db: Session = Depends(get_db)):
    e = ep_service.get_single_ep(db=db, id=id)
    return e


@router.get('/patient/ep/', response_model=List[Union[ResultInt, List[EpOutWithDoctorName]]])
def patient_prescriptions(skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    e = ep_service.patient_prescriptions(db=db, skip=skip, limit=limit, descending=True, count_results=True, patient_id=current_user.id)
    return handle_result(e)


@router.get('/doctor/ep/', response_model=List[Union[ResultInt, List[EpOutWithDoctorName]]])
def doctor_prescriptions(start_date: str = beginning_date, end_date: str = current_date, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    e = ep_service.doctor_prescriptions(db=db, start_date=start_date, end_date=end_date, skip=skip, limit=limit, descending=True, count_results=True, doctor_id=current_user.id)
    return handle_result(e)

### antor ### 
@router.get('/all/ep/', response_model=List[Union[ResultInt, List[EpOutWithDoctorName]]])
def all_prescriptions(start_date: str = beginning_date, end_date: str = current_date, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    e = ep_service.all_prescriptions(db=db, start_date=start_date, end_date=end_date, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(e)

# @router.get('/single/ep/{user_id}', response_model=List[Union[ResultInt, List[EpOutWithDoctorName]]])
# def single_prescription_by_id(user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
#     e = ep_service.single_prescription_by_id(db=db, user_id=user_id, skip=skip, limit=limit, descending=True, count_results=True)
#     return handle_result(e)