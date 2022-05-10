from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import DoctorOut, DoctorSpecialityOut, DoctorQualificationOut, DoctorSpecialityOut, DoctorQualilficationUpdate, DoctorSpecialityUpdate, DoctorSignup, UserOut, UserOutAuth
from services import doctors_service, doctor_qualifications_service, doctor_specialities_service
from api.v1.auth_dependcies import logged_in_doctor


router = APIRouter()


@router.post('/signup', response_model=DoctorSpecialityOut)
def signup(doctor_in: DoctorSignup, db: Session = Depends(get_db)):
    doctor = doctors_service.signup(db, data_in=doctor_in)
    return handle_result(doctor)


@router.get('/auth', response_model=UserOutAuth)
def auth(doctor: Session = Depends(logged_in_doctor)):
    return doctor


@router.get('/',response_model=DoctorOut)
def get_doctor(db: Session = Depends(get_db), current_user: Session= Depends(logged_in_doctor)):
    doc = doctors_service.get_by_user_id(db=db, user_id=current_user.id)
    return handle_result(doc)


@router.get('/qualifications', response_model=DoctorQualificationOut)
def get(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    qualification = doctor_qualifications_service.get_by_user_id(
        db, user_id=current_user.id)
    return handle_result(qualification)


@router.put('/qualifications/{id}', response_model=DoctorQualificationOut)
def update(id: int, data_update: DoctorQualilficationUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    qualification = doctor_qualifications_service.update(db, id, data_update)
    return handle_result(qualification)


@router.get('/specialities', response_model=DoctorSpecialityOut)
def get(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    speciality = doctor_specialities_service.get_by_user_id(
        db, user_id=current_user.id)
    return handle_result(speciality)


@router.put('/specialities/{id}', response_model=DoctorSpecialityOut)
def update(id: int, data_update: DoctorSpecialityUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    speciality = doctor_specialities_service.update(db, id, data_update)
    return handle_result(speciality)
