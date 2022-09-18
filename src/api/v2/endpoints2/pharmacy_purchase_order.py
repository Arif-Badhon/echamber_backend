from fastapi import APIRouter, Depends
from schemas import PharmacyPurchaseOrderWithSingleOrder
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_purchase_order_service
from exceptions.service_result import handle_result

router = APIRouter()

@router.post("/")
def pharmacy_purchase_order_with_singleorder(data_in: PharmacyPurchaseOrderWithSingleOrder, db: Session = Depends(get_db)):
    order = pharmacy_purchase_order_service.submit(db=db, data_in=data_in)
    return handle_result (order)