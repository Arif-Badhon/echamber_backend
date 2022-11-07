from fastapi import APIRouter, Depends
from schemas import PharmacyInvoiceWithSingleInvoice, PharmacyInvoiceOut, ResultInt, PharmacySingleInvoiceOut, PharmacySingleInvoiceWithMedicine
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_invoice_service, pharmacy_single_invoice_service
from exceptions.service_result import handle_result
from api.v2.auth_dependcies import logged_in_pharmacy_admin
from typing import List, Union

router = APIRouter()

@router.post('/')
def invoice_with_single_invoice(data_in: PharmacyInvoiceWithSingleInvoice, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    invoice = pharmacy_invoice_service.create_invoice(db=db, data_in=data_in, user_id = current_user.id)
    return handle_result(invoice)


@router.get('/', response_model=List[Union[ResultInt, List[PharmacyInvoiceOut]]])
def get_all_invoice(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    get_invoice = pharmacy_invoice_service.get_with_pagination(db = db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(get_invoice)


@router.get('/single-invoice/{id}', response_model=List[Union[ResultInt, List[PharmacySingleInvoiceWithMedicine]]])
def get_single_invoice_with_invoice_id(id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    search_single_invoice = pharmacy_single_invoice_service.all_single_invoice(db=db, skip=skip, limit=limit, invoice_id = id)
    return handle_result(search_single_invoice)