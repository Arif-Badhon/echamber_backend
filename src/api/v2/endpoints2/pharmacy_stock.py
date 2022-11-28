from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from schemas import PharmacyEverySingleStockOutWithMedicine, PharmacyTotalCurrentStockWithMedicine, PharmacyTotalCurrentStockOut, PharmacyTotalCurrentStockUpdate, ResultInt
from services import pharmacy_every_single_stock_servive, pharmacy_total_current_stock_service
from typing import List, Union
from repositories import pharmacy_every_single_stock_repo

router = APIRouter()


@router.get("/every-single-stock/", response_model=List[PharmacyEverySingleStockOutWithMedicine])
def get_single_stock(db: Session = Depends(get_db)):
    search_single = pharmacy_every_single_stock_servive.all_single_stock(db=db)
    return handle_result(search_single)


@router.get("/total-current-stock/{pharmacy_id}", response_model=List[Union[ResultInt, List[PharmacyTotalCurrentStockWithMedicine]]])
def get_total_stock(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_total = pharmacy_total_current_stock_service.total_current_stock(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return handle_result(search_total)


@router.patch('/update-total-stock/{id}', response_model=PharmacyTotalCurrentStockOut)
def update_total_stock(id: int, data_update: PharmacyTotalCurrentStockUpdate, db: Session = Depends(get_db)):
    update_total_stock = pharmacy_total_current_stock_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_total_stock)


@router.get('/expired-medicines/{pharmacy_id}', response_model=List[Union[ResultInt, List[PharmacyEverySingleStockOutWithMedicine]]])
def expired_medicine(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    em = pharmacy_every_single_stock_servive.get_expired_medicine(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return handle_result(em)


@router.get('/nearly-expired-medicines/{pharmacy_id}')
def nearly_expired_medicine(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    nem = pharmacy_every_single_stock_servive.get_nearly_expired_medicine(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return handle_result(nem)