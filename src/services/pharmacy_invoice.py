from services import BaseService, pharmacy_service
from models import PharmacyInvoice
from schemas import PharmacyInvoiceIn, PharmacyInvoiceUpdate, PharmacyInvoiceWithSingleInvoice, PharmacySingleInvoiceWithInvoice, PharmacyTotalCurrentStockUpdate
from repositories import pharmacy_invoice_repo, pharmacy_single_invoice_repo, pharmacy_total_current_stock_repo
from sqlalchemy.orm import Session
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException
from fastapi import status

class PharmacyInvoiceService(BaseService[PharmacyInvoice, PharmacyInvoiceIn, PharmacyInvoiceUpdate]):
    def create_invoice(self, data_in:PharmacyInvoiceWithSingleInvoice , db: Session, user_id: int):
        validate_user = pharmacy_service.check_user_with_pharmacy(db=db, user_id=user_id, pharmacy_id=data_in.invoice.pharmacy_id)
        if validate_user == False:
            return ServiceResult(AppException.ServerError("Invalid Pharmacy ID"))
        invoice = pharmacy_invoice_repo.create_with_flush(db=db, data_in=PharmacyInvoiceIn(
            subtotal_amount=data_in.invoice.subtotal_amount,
            total_amount_mrp=data_in.invoice.total_amount_mrp,
            total_amount=data_in.invoice.total_amount,
            paid_amount=data_in.invoice.paid_amount,
            due_amount=data_in.invoice.due_amount,
            remarks=data_in.invoice.remarks,
            discount=data_in.invoice.discount,
            vat=data_in.invoice.vat,
            invoice_number=data_in.invoice.invoice_number,
            customer_id=data_in.invoice.customer_id,
            pharmacy_id=data_in.invoice.pharmacy_id
        ))

        if data_in.single_invoice and len(data_in.single_invoice) != 0:
            for i in data_in.single_invoice:
                invoice_single = pharmacy_single_invoice_repo.create_with_flush(db=db, data_in=PharmacySingleInvoiceWithInvoice(
                    mrp=i.mrp,
                    quantity=i.quantity,
                    unit_prize=i.unit_prize,
                    discount=i.discount,
                    cost=i.cost,
                    medicine_id=i.medicine_id,
                    pack_size=i.pack_size,
                    invoice_id=invoice.id
                ))

                check_medicine_pharmacy_id = pharmacy_total_current_stock_repo.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=True, medicine_id =i.medicine_id, pharmacy_id=invoice.pharmacy_id)
                if check_medicine_pharmacy_id[0]["results"] != 0:
                    update_total_stock = pharmacy_total_current_stock_repo.update(db=db, id=check_medicine_pharmacy_id[1][0].id, data_update=PharmacyTotalCurrentStockUpdate(
                        quantity=check_medicine_pharmacy_id[1][0].quantity - invoice_single.quantity
                    ))

                else:
                    return ServiceResult(AppException.ServerError("Empty Medicine"))

        db.commit()

        return ServiceResult({"msg": "Success"}, status_code=200)


    def get_invoice_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        get_invoice = self.repo.get_invoice_by_pharmacy_id(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
        return get_invoice

    def invoice_filter(self, db: Session, pharmacy_id: int, customer_id: int, start_date: str, end_date: str, single_date: str, skip: int, limit: int):
        get_invoice = self.repo.invoice_filter(db=db, pharmacy_id=pharmacy_id, customer_id=customer_id, start_date=start_date, end_date=end_date, single_date=single_date, skip=skip, limit=limit)
        if not get_invoice:
            return ServiceResult(AppException.ServerError("No data found"))
        return ServiceResult(get_invoice, status_code=status.HTTP_201_CREATED)

    def get_total_sale(self, db: Session, pharmacy_id: int, customer_id: int, start_date: str, end_date: str):
        get_sale = self. repo.get_total_sale(db=db, pharmacy_id=pharmacy_id, customer_id=customer_id, start_date=start_date, end_date=end_date)
        return get_sale


pharmacy_invoice_service = PharmacyInvoiceService(PharmacyInvoice, pharmacy_invoice_repo)