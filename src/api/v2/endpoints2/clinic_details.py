from typing import List
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ClinicDetailsIn, ClinicNavbarIn
from db import get_db
from sqlalchemy.orm import Session
from services import clinic_details_service, clinic_navbar_service


router = APIRouter()


@router.get("/")
def get_clinic_details(db: Session = Depends(get_db)):
    get_clinic_details = clinic_details_service.get(db=db)
    return handle_result(get_clinic_details)


@router.post("/clinic-details/")
def add_clinic_details(data_in: ClinicDetailsIn, db: Session = Depends(get_db)):
    cd = clinic_details_service.create(db=db, data_in=data_in)
    return handle_result(cd)

@router.post("/clinic-details/navbar")
def add_clinic_nav(data_in: ClinicNavbarIn, db: Session = Depends(get_db)):
    cn = clinic_navbar_service.create(db=db, data_in=data_in)
    return handle_result(cn)
