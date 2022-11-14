from typing import List, Union
from fastapi import APIRouter, Depends
from schemas import PharmacyGrnWithSingleGrn, ResultInt, PharmacyGrnOut, PharmacySingleGrnWithMedicine, PharmacyGrnUpdate, PharmacySingleGrnOut, PharmacySingleGrnUpdate
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_grn_service, pharmacy_single_grn_service
from exceptions.service_result import handle_result
from api.v2.auth_dependcies import logged_in_pharmacy_admin

router = APIRouter()

@router.post("/")
def grn_with_single_grn(data_in: PharmacyGrnWithSingleGrn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    grn = pharmacy_grn_service.submit(db=db, data_in=data_in, user_id = current_user.id)
    return handle_result (grn)


@router.get("/get-grn-by-pharmacy-id/{id}", response_model=List[Union[ResultInt, List[PharmacyGrnOut]]])
def get_grn_by_pharmacy(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_grn = pharmacy_grn_service.get_grn_by_pharmacy_id(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return search_grn


@router.get("/single/{id}", response_model=List[Union[ResultInt, List[PharmacySingleGrnWithMedicine]]])
def search_single_grn(id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single_grn = pharmacy_single_grn_service.all_single_grn(db=db, skip=skip, limit=limit, grn_id = id)
    return handle_result(search_single_grn)


@router.patch('/update-grn{id}', response_model=PharmacyGrnOut)
def update_grn(id: int, data_update: PharmacyGrnUpdate, db: Session = Depends(get_db)):
    update_grn = pharmacy_grn_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_grn)


@router.patch('/update-single-grn/{id}', response_model=PharmacySingleGrnOut)
def update_single_grn(id: int, data_update: PharmacySingleGrnUpdate, db: Session = Depends(get_db)):
    update_single_grn = pharmacy_single_grn_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_single_grn)