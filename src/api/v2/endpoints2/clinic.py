from typing import List, Union
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ClinicOut, ClinicUserWithClinic, Token, ClinicLogin,ClinicWithDoctorDetails, ClinicUserHxId, ResultInt, DoctorSignup
from db import get_db
from sqlalchemy.orm import Session
from services import clinic_service, clinic_with_doctor_service
from api.v2.auth_dependcies import logged_in_admin, logged_in_clinic_admin

router = APIRouter()


@router.get("/", response_model=List[ClinicOut])
def get_clinic(db: Session = Depends(get_db)):
    get_all_clinic = clinic_service.get(db=db)
    return handle_result(get_all_clinic)


@router.post("/signup", response_model=ClinicUserHxId)
def clinic_register_by_admin(data_in: ClinicUserWithClinic, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    admin = clinic_service.register_clinic(db=db, data_in=data_in)
    return handle_result(admin)


@router.post("/signup/user", response_model=ClinicUserHxId)
def clinic_register_by_user(data_in: ClinicUserWithClinic, db: Session = Depends(get_db)):
    user = clinic_service.register_clinic(db=db, data_in=data_in)
    return handle_result(user)


@router.post("/login", response_model=Token)
def clinic_login_by_user(data_in: ClinicLogin, db: Session = Depends(get_db)):
    login = clinic_service.clinic_user_login(db=db, data_in=data_in)
    return handle_result(login)


@router.post('/doctor-append/{doctor_user_id}/{clinic_id}')
def append_doctor(doctor_user_id: int, clinic_id:int,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    append_doc = clinic_with_doctor_service.doctor_append(db=db, doctor_user_id=doctor_user_id, clinic_id=clinic_id, user_id = current_user.id)
    return handle_result(append_doc)


@router.get("/user-clinic-id")
def search_with_user_and_clinic_id(user_id: int, clinic_id: int, db: Session = Depends(get_db)):
    check = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=clinic_id)
    return check 


# @router.get('/get-clinic-doctors-id', response_model= List[Union[ResultInt, List[ClinicIdWithDoctorIdOut]]])
# def get_doctors_in_clinic(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
#     get_doc = clinic_with_doctor_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
#     return handle_result(get_doc)


@router.get('/search-doctor-by-clinic_id', response_model= List[Union[ResultInt, List[ClinicWithDoctorDetails]]])
def doctor_list(clinic_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    sc = clinic_with_doctor_service.search_by_clinic_id(db=db, skip=skip, limit=limit, clinic_id=clinic_id)
    return sc


@router.post('/clinic-doctor-signup')
def doctor_registration_by_clinic(doctor_in: DoctorSignup, clinic_id: int,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    doctor = clinic_service.clinic_doctor_signup(db=db, data_in=doctor_in, clinic_id=clinic_id, user_id = current_user.id)
    return handle_result(doctor)
