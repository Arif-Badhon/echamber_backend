from typing import List, Union
from fastapi import APIRouter, Depends
from schemas import PharmacyGrnWithSingleGrn, ResultInt, PharmacyGrnOut, PharmacySingleGrnOut
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_grn_service, pharmacy_single_grn_service
from exceptions.service_result import handle_result

router = APIRouter()

@router.post("/")
def grn_with_single_grn(data_in: PharmacyGrnWithSingleGrn, db: Session = Depends(get_db)):
    grn = pharmacy_grn_service.submit(db=db, data_in=data_in)
    return handle_result (grn)


@router.get("/", response_model=List[Union[ResultInt, List[PharmacyGrnOut]]])
def search_grn(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_grn = pharmacy_grn_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(search_grn)


@router.get("/single/{id}", response_model=List[Union[ResultInt, List[PharmacySingleGrnOut]]])
def search_single_grn(id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single_grn = pharmacy_single_grn_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, grn_id = id)
    return handle_result(search_single_grn)