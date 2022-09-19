from fastapi import APIRouter, Depends
from schemas import PharmacyGrnWithSingleGrn
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_grn_service
from exceptions.service_result import handle_result

router = APIRouter()

@router.post("/")
def grn_with_single_grn(data_in: PharmacyGrnWithSingleGrn, db: Session = Depends(get_db)):
    grn = pharmacy_grn_service.submit(db=db, data_in=data_in)
    return handle_result (grn)