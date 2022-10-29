from fastapi import APIRouter, Depends
from schemas import PharmacyInvoiceWithSingleInvoice
from db import get_db
from sqlalchemy.orm import Session
from services import pharmacy_invoice_service
from exceptions.service_result import handle_result
from api.v2.auth_dependcies import logged_in_pharmacy_admin

router = APIRouter()

@router.post('/')
def invoice_with_single_invoice(data_in: PharmacyInvoiceWithSingleInvoice, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_pharmacy_admin)):
    invoice = pharmacy_invoice_service.create_invoice(db=db, data_in=data_in, user_id = current_user.id)
    return handle_result(invoice)