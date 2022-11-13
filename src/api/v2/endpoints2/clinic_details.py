from typing import List
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ClinicDetailsIn, ClinicNavbarIn, ClinicServicesIn, ClinicOfferIn, ClinicDetailsOut, ClinicDetailsUpdate, ClinicNavbarOut, ClinicNavbarUpdate
from db import get_db
from sqlalchemy.orm import Session
from services import clinic_details_service, clinic_navbar_service, clinic_service_service, clinic_offer_service
from api.v2.auth_dependcies import logged_in_clinic_admin


router = APIRouter()


# @router.get("/")
# def get_clinic_details(db: Session = Depends(get_db)):
#     get_clinic_details = clinic_details_service.get(db=db)
#     return handle_result(get_clinic_details)


@router.post("/clinic-details/")
def add_clinic_details(data_in: ClinicDetailsIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    cd = clinic_details_service.clinic_details_add(db=db, data_in=data_in, user_id= current_user.id)
    return handle_result(cd)


@router.get("/clinic-detais-by-id", response_model=List[ClinicDetailsOut])
def get_clinic_details_by_clinic_id(clinic_id: int, db: Session = Depends(get_db)):
    get_clinic_details = clinic_details_service.get_details_by_clinic_id(db=db, clinic_id=clinic_id)
    return get_clinic_details


@router.patch('/update-clinic-details/{id}', response_model=ClinicDetailsOut)
def update_clinic_details(id: int, data_update: ClinicDetailsUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    update_clinic_details = clinic_details_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_clinic_details)



@router.post("/clinic-details/navbar")
def add_clinic_nav(data_in: ClinicNavbarIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    cn = clinic_navbar_service.clinic_nav(db=db, data_in=data_in, user_id= current_user.id)
    return handle_result(cn)
    
    
@router.get("/clinic-navbar-by-id", response_model=List[ClinicNavbarOut])
def get_nav_by_clinic_id(clinic_id: int, db: Session = Depends(get_db)):
    get_clinic_nav = clinic_navbar_service.get_nav_by_clinic_id(db=db, clinic_id=clinic_id)
    return get_clinic_nav


@router.patch('/update-clinic-nav/{id}', response_model=ClinicNavbarOut)
def update_clinic_nav(id: int, data_update: ClinicNavbarUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
    update_nav = clinic_navbar_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_nav)


# @router.post("/clinic-service")
# def add_clinic_service(data_in: ClinicServicesIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
#     cs = clinic_service_service.create(db=db, data_in=data_in)
#     return handle_result(cs)


# @router.post("/clinic-offer")
# def add_clinic_offer(data_in: ClinicOfferIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_clinic_admin)):
#     cf = clinic_offer_service.create(db=db, data_in=data_in)
#     return handle_result(cf)