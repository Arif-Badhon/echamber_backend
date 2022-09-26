from multiprocessing.forkserver import read_signed
from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from schemas import PharmacyEverySingleStockOut
from schemas.pharmacy_stock import PharmacyTOtalCurrentStockOut
from services import pharmacy_every_single_stock_servive, pharmacy_total_current_stock_service

router = APIRouter()

@router.get("/every-single-stock/", response_model=PharmacyEverySingleStockOut)
def search(db: Session = Depends(get_db)):
    search_single = pharmacy_every_single_stock_servive.get(db=db)
    return handle_result(search_single)


@router.get("/total-current-stock/", response_model=PharmacyTOtalCurrentStockOut)
def search(db: Session = Depends(get_db)):
    search_total = pharmacy_total_current_stock_service.get(db=db)
    return handle_result(search_total)