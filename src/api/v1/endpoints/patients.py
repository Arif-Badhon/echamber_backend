from typing import List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_patient
from exceptions import handle_result
from schemas import PatientOut, PatientSignup, UserDetailOut, NewPasswordIn, Token, ServiceOrderOut, ResultInt, AdminPanelActivityOut, ServiceOrderIn, MedicineOrderIn
from db import get_db
from schemas import PatientBase, UserOut, UserOutAuth
from schemas.medicine_order import MedicineOrderOut
from services import patients_service, service_order_service, medicine_order_service

router = APIRouter()


@router.post('/signup/', response_model=UserDetailOut)
def signup(patient_in: PatientSignup, db: Session = Depends(get_db)):
    patient = patients_service.signup(db, data_in=patient_in)
    return handle_result(patient)


@router.get('/auth', response_model=UserOutAuth)
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


@router.get('/services', response_model=List[Union[ResultInt, List[ServiceOrderOut]]])
def all_services(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    services = service_order_service.get_by_key(
        db=db, skip=skip, limit=limit, descending=True, count_results=True, patient_id=current_user.id)
    return handle_result(services)


@router.post('/service/medicines', response_model=AdminPanelActivityOut)
def medicine_order(data_in: List[Union[ServiceOrderIn, List[MedicineOrderIn]]], db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    medicine_order = service_order_service.medicine_order(
        db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(medicine_order)


@router.get('/service/medicines/{service_id}', response_model=List[Union[ResultInt, List[MedicineOrderOut]]])
def medicine_order_by_service(service_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    data = medicine_order_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=True, service_order_id=service_id)
    return handle_result(data)
