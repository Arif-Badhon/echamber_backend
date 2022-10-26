from typing import List
from fastapi import APIRouter, Depends
# from api.v1.endpoints.doctor_chambers import get
from exceptions.service_result import handle_result
from schemas import ClinicOut, ClinicUserWithClinic, Token, ClinicLogin, ClinicUserHxId
from db import get_db
from sqlalchemy.orm import Session
from services import clinic_service
from api.v2.auth_dependcies import logged_in_admin

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
def clinic_siguup_user(data_in: ClinicUserWithClinic, db: Session = Depends(get_db)):
    user = clinic_service.register_clinic(db=db, data_in=data_in)
    return handle_result(user)


@router.post("/login", response_model=Token)
def clinic_user_login(data_in: ClinicLogin, db: Session = Depends(get_db)):
    login = clinic_service.clinic_user_login(db=db, data_in=data_in)
    return handle_result(login)
