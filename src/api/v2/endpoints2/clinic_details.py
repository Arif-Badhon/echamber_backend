from typing import List
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ClinicDetailsIn, ClinicNavbarIn, ClinicServicesIn, ClinicOfferIn
from db import get_db
from sqlalchemy.orm import Session
from services import clinic_details_service, clinic_navbar_service, clinic_service_service, clinic_offer_service
from api.v2.auth_dependcies import logged_in_clinic_admin


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


@router.post("/clinic-service")
def add_clinic_service(data_in: ClinicServicesIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    cs = clinic_service_service.create(db=db, data_in=data_in)
    return handle_result(cs)


@router.post("/clinic-offer")
def add_clinic_offer(data_in: ClinicOfferIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    cf = clinic_offer_service.create(db=db, data_in=data_in)
    return handle_result(cf)