from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_patient
from exceptions import handle_result
from schemas import PatientOut, PatientSignup, UserDetailOut
from db import get_db
from schemas import PatientBase, UserOut
from services import patients_service

router = APIRouter()


# @router.get('/', response_model=List[PatientOut])
# def get(db: Session = Depends(get_db)):
#     patients = patients_service.get(db)
#     return handle_result(patients)


@router.post('/signup/', response_model=UserDetailOut)
def signup(patient_in: PatientSignup, db: Session = Depends(get_db)):
    patient = patients_service.signup(db, data_in=patient_in)
    return handle_result(patient)


@router.get('/auth', response_model=UserOut)
def auth(patient: Session = Depends(logged_in_patient)):
    return patient


@router.get('/', response_model=PatientOut)
def get_patient(db: Session = Depends(get_db), current_user=Depends(logged_in_patient)):
    patient = patients_service.get_by_user_id(db, user_id=current_user.id)
    return handle_result(patient)


@router.put('/', response_model=PatientOut)
def update(patient_update: PatientBase, db: Session = Depends(get_db), current_user=Depends(logged_in_patient)):
    patient = patients_service.update_by_user_id(
        db, user_id=current_user.id, data_update=patient_update)
    return handle_result(patient)
