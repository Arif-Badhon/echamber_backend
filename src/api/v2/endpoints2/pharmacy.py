from typing import List
from fastapi import APIRouter, Depends
from schemas import PharmacyOut, PharmacyUserWithPharmacy, Token, PharmacyLogin, PharmacyUpdate, UserOutAuth, PharmacyUserOut, PharmacyUserWithPharmacyID
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_service
from exceptions.service_result import handle_result
from api.v2.auth_dependcies import logged_in, logged_in_admin
from models import User

router = APIRouter()


@router.get("/trade-license", response_model=PharmacyOut)
def search_with_trade_license(trade_license: str, db: Session = Depends(get_db)):
    trade = pharmacy_service.search_by_trade_license(db=db, trade_license=trade_license)
    return handle_result(trade)


@router.post("/signup")
def pharmacy_register_by_admin(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    admin = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(admin)

@router.post("/signup/user")
def pharmacy_user_signup(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db)):
    user = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(user)

@router.post("/login", response_model=Token)
def pharmacy_user_login(data_in: PharmacyLogin, db: Session = Depends(get_db)):
    login = pharmacy_service.pharmacy_user_login(db=db, data_in=data_in)
    return handle_result(login)


@router.patch('/{id}', response_model=PharmacyOut)
def update_pharmacy(id: int, data_update: PharmacyUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    update_ph = pharmacy_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_ph)


@router.get('/auth', response_model=UserOutAuth)
def auth(current_user: User = Depends(logged_in)):
    return current_user


@router.get("/user-pharmacy-id")
def search_with_user_and_pharmacy_id(user_id: int, pharmacy_id: int, db: Session = Depends(get_db)):
    check = pharmacy_service.check_user_with_pharmacy(db=db, user_id=user_id, pharmacy_id=pharmacy_id)
    return check 


@router.get("/user-pharmacy")
def search_pharmacy_with_user_id(user_id: int, db: Session = Depends(get_db)):
    search = pharmacy_service.find_pharmacy_with_user_id(db=db, user_id=user_id)
    return handle_result(search)