from fastapi import APIRouter, Depends
from schemas import PharmacyPurchaseOrderWithSingleOrder, PharmacyPurchaseOrderOut, PharmacyPurchaseSingleOrderOut, ResultInt
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_purchase_order_service, pharmacy_purchase_single_order_service
from exceptions.service_result import handle_result
from typing import List, Union

router = APIRouter()

@router.post("/")
def pharmacy_purchase_order_with_singleorder(data_in: PharmacyPurchaseOrderWithSingleOrder, db: Session = Depends(get_db)):
    order = pharmacy_purchase_order_service.submit(db=db, data_in=data_in)
    return handle_result (order)


@router.get("/", response_model=List[Union[ResultInt, List[PharmacyPurchaseOrderOut]]])
def search_purchase_order(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search = pharmacy_purchase_order_service.get_with_pagination(db = db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(search)


@router.get("/single/{id}", response_model=List[Union[ResultInt, List[PharmacyPurchaseSingleOrderOut]]])
def search_single_purchase_order(id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single = pharmacy_purchase_single_order_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, purchase_order_id = id)
    return handle_result(search_single)