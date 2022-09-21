from typing import List
from fastapi import APIRouter, Depends
from schemas import PharmacyOut, PharmacyUserWithPharmacy, Token, PharmacyLogin
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_service
from exceptions.service_result import handle_result
from api.v1.auth_dependcies import logged_in_admin

router = APIRouter()


@router.get("/trade-license", response_model=PharmacyOut)
def search_with_trade_license(trade_license: str, db: Session = Depends(get_db)):
    trade = pharmacy_service.search_by_trade_license(db=db, trade_license=trade_license)
    return handle_result(trade)


@router.post("/signup")
def pharmacy_register_by_admin(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    admin = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(admin)


@router.post("/login", response_model=Token)
def pharmacy_user_login(data_in: PharmacyLogin, db: Session = Depends(get_db)):
    login = pharmacy_service.pharmacy_user_login(db=db, data_in=data_in)
    return handle_result(login)
