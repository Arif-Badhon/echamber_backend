from fastapi import APIRouter, Depends
from schemas import PharmacyPurchaseOrderWithSingleOrder, PharmacyPurchaseOrderOut, PharmacyPurchaseSingleOrderOut, ResultInt, PharmacyPurchaseOrderUpdate, PharmacyPurchaseSingleOrderWithMedicine
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_purchase_order_service, pharmacy_purchase_single_order_service
from exceptions.service_result import handle_result
from typing import List, Union
from api.v2.auth_dependcies import logged_in_pharmacy_admin

router = APIRouter()

@router.post("/")
def pharmacy_purchase_order_with_singleorder(data_in: PharmacyPurchaseOrderWithSingleOrder, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    order = pharmacy_purchase_order_service.submit(db=db, data_in=data_in, user_id = current_user.id)
    return handle_result (order)


@router.get("/get-by_pharmacy_id", response_model=List[Union[ResultInt, List[PharmacyPurchaseOrderOut]]])
def get_all_purchase_order(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search = pharmacy_purchase_order_service.get_purchase_order_by_pharmacy_id(db = db,pharmacy_id= pharmacy_id, skip=skip, limit=limit)
    return search


@router.get("/single-order-with-purchase-id/{id}", response_model=List[Union[ResultInt, List[PharmacyPurchaseSingleOrderWithMedicine]]])
def get_single_purchase_order(id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single = pharmacy_purchase_single_order_service.all_single_order(db=db, skip=skip, limit=limit, purchase_order_id = id)
    return handle_result(search_single)


@router.patch('/{id}', response_model=PharmacyPurchaseOrderOut)
def update_purchase_order(id: int, data_update: PharmacyPurchaseOrderUpdate, db: Session = Depends(get_db)):
    update_pho = pharmacy_purchase_order_service.update(db=db, data_update=data_update, id=id)
    return handle_result(update_pho)



@router.get("/single-order-with-purchase-num/", response_model=List[Union[ResultInt, List[PharmacyPurchaseSingleOrderWithMedicine]]])
def get_single_purchase_order(purchase_number: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single = pharmacy_purchase_single_order_service.all_single_order_by_purchase_num(db=db, skip=skip, limit=limit, purchase_number= purchase_number)
    return handle_result(search_single)

# , response_model=List[Union[ResultInt, List[PharmacyPurchaseOrderOut]]]
@router.get("/purchase-order-with-grn")
def get_all_purchase_order_with_grn(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search = pharmacy_purchase_order_service.get_purchase_order_with_grn(db = db, skip=skip, limit=limit)
    return search

@router.get('/purchase-order-with-purchase-num/', response_model=List[Union[ResultInt, List[PharmacyPurchaseOrderOut]]])
def get_purchase_order(purchase_number: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_purchase_order = pharmacy_purchase_single_order_service.purchase_oder_by_purchase_num(db=db, skip=skip, limit=limit, purchase_number= purchase_number)
    return handle_result(search_purchase_order)

@router.get("/purchase-order-without-grn", response_model=List[Union[ResultInt, List[PharmacyPurchaseOrderOut]]])
def get_all_purchase_order_without_grn(pharmacy_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search = pharmacy_purchase_order_service.get_purchase_order_without_grn(db = db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
    return search