from typing import List, Union
from fastapi import APIRouter, Depends
from schemas import PharmacyOut, PharmacyUserWithPharmacy, Token, PharmacyLogin, PharmacyUpdate, UserOutAuth, PharmacyUserHxId, PatientSignup, ResultInt, PharmacyActivityOut, PharmacyActivityOutWithUser
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_service, pharmacy_activity_service
from exceptions.service_result import handle_result
from api.v2.auth_dependcies import logged_in, logged_in_admin, logged_in_pharmacy_admin
from models import User

router = APIRouter()


@router.get("/trade-license", response_model=PharmacyOut)
def search_with_trade_license(trade_license: str, db: Session = Depends(get_db)):
    trade = pharmacy_service.search_by_trade_license(db=db, trade_license=trade_license)
    return handle_result(trade)


@router.post("/signup", response_model=PharmacyUserHxId)
def pharmacy_register_by_admin(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    admin = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(admin)

@router.post("/signup/user", response_model=PharmacyUserHxId)
def pharmacy_user_signup(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db)):
    user = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(user)

@router.post("/login", response_model=Token)
def pharmacy_user_login(data_in: PharmacyLogin, db: Session = Depends(get_db)):
    login = pharmacy_service.pharmacy_user_login(db=db, data_in=data_in)
    return handle_result(login)


@router.patch('/{id}', response_model=PharmacyOut)
def update_pharmacy(id: int, data_update: PharmacyUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    update_ph = pharmacy_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_ph)


@router.get('/auth', response_model=UserOutAuth)
def auth(current_user: User = Depends(logged_in)):
    return current_user


@router.get("/user-pharmacy-id")
def search_with_user_and_pharmacy_id(user_id: int, pharmacy_id: int, db: Session = Depends(get_db)):
    check = pharmacy_service.check_user_with_pharmacy(db=db, user_id=user_id, pharmacy_id=pharmacy_id)
    return check 


@router.get("/user-pharmacy", response_model=PharmacyOut)
def search_pharmacy_with_user_id(user_id: int, db: Session = Depends(get_db)):
    search = pharmacy_service.find_pharmacy_with_user_id(db=db, user_id=user_id)
    return handle_result(search)



@router.post('/pharmacy-patient-registartion')
def patient_registration_by_pharmacy(patient_in: PatientSignup, pharmacy_id: int,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    patient = pharmacy_service.pharmacy_patient_signup(db=db, data_in=patient_in, pharmacy_id=pharmacy_id, user_id = current_user.id)
    return handle_result(patient)



@router.get('/activity/log-pharmacy-by_pharmacy_id/', response_model=List[Union[ResultInt, List[PharmacyActivityOut]]])
def pharmacy_activity_log(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    activity = pharmacy_activity_service.get_activity_by_pharmacy_id(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return activity


@router.get('/get_pharmacy_patient/' , response_model=List[Union[ResultInt, List[PharmacyActivityOutWithUser]]])
def get_pharmacy_patient_list(pharmacy_id: int, skip: int=0, limit: int = 10, db: Session = Depends(get_db)):
    get_patient = pharmacy_activity_service.get_pharmacy_patient(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return get_patient
