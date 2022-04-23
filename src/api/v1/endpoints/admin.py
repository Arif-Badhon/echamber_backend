from typing import List
from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreateWitoutRole, UserDoctorOut, DoctorChamberOut
from sqlalchemy.orm import Session
from services import admin_service, doctor_chambers_service
from api.v1.auth_dependcies import logged_in_admin, logged_in_admin_moderator, logged_in_moderator


router = APIRouter()


@router.get('/auth', response_model=UserOut)
def auth(auth: Session = Depends(logged_in_admin_moderator)):
    return auth

@router.get('/auth/admin', response_model=UserOut)
def admin_auth(admin: Session = Depends(logged_in_admin)):
    return admin


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)


@router.get('/all/moderator', response_model=List[UserOut])
def all_moderators(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    all = admin_service.all_moderator(db)
    return handle_result(all)


@router.get('/auth/moderator', response_model=UserOut)
def moderator_auth(moderator: Session = Depends(logged_in_moderator)):
    return moderator


@router.post('/create/moderator', response_model=UserOut)
def moderator_create(data_in: UserCreateWitoutRole, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    moderator = admin_service.signup_moderator(db, data_in=data_in)
    return handle_result(moderator)


@router.get('/active/doctors', response_model=List[UserDoctorOut])
def doctors_active_list(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    docs = admin_service.doctor_active_list(db)
    return handle_result(docs)


@router.get('/inactive/doctors', response_model=List[UserDoctorOut])
def doctors_inactive_list(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    docs = admin_service.doctor_inactive_list(db)
    return handle_result(docs)


@router.put('/doctor/activate', response_model=UserOut)
def doctor_active(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    doc = admin_service.doctor_active_id(db=db, id=id)
    return handle_result(doc)


@router.get('/doctor/chambers/{user_id}',response_model=List[DoctorChamberOut])
def chamber_list(user_id :int,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    chambers =  doctor_chambers_service.get_by_user_id(db=db, user_id=user_id)
    return handle_result(chambers)