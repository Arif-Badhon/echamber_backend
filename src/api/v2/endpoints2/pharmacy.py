from typing import List
from fastapi import APIRouter, Depends
from schemas import PharmacyOut, PharmacyUserWithPharmacy
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_service
from exceptions.service_result import handle_result
from api.v1.auth_dependcies import logged_in_admin

router = APIRouter()

@router.get("/", response_model=List[PharmacyOut])
def search(db: Session = Depends(get_db)):
    pharma = pharmacy_service.get(db=db)
    return handle_result(pharma)

@router.post("/")
def pharmacy_with_user(data_in: PharmacyUserWithPharmacy, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    user = pharmacy_service.register_pharmacy(db=db, data_in=data_in)
    return handle_result(user)