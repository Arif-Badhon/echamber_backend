from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from schemas import PharmacyEverySingleStockOutWithMedicine, PharmacyTotalCurrentStockWithMedicine
from services import pharmacy_every_single_stock_servive, pharmacy_total_current_stock_service
from typing import List

router = APIRouter()


@router.get("/every-single-stock/", response_model=List[PharmacyEverySingleStockOutWithMedicine])
def get_single_stock(db: Session = Depends(get_db)):
    search_single = pharmacy_every_single_stock_servive.all_single_stock(db=db)
    return handle_result(search_single)


@router.get("/total-current-stock/", response_model=List[PharmacyTotalCurrentStockWithMedicine])
def get_total_stock(db: Session = Depends(get_db)):
    search_total = pharmacy_total_current_stock_service.total_current_stock(db=db)
    return handle_result(search_total)