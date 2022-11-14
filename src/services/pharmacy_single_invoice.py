from services import BaseService
from models import PharmacySingleInvoice
from schemas import PharmacySingleInvoiceIn, PharmacySingleInvoiceUpdate
from repositories import pharmacy_single_invoice_repo, ep_medicines_list_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result


class PhamrmacySingleInvoiceService(BaseService[PharmacySingleInvoice, PharmacySingleInvoiceIn, PharmacySingleInvoiceUpdate]):
     def all_single_invoice(self, db: Session, skip: int, limit: int, invoice_id: int):
        all_single_invoice = self.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, invoice_id=invoice_id)
        data = []

        for i in handle_result(all_single_invoice)[1]:
            med_id = i.medicine_id
            medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
            i.medicine_name = medicines.name
            i.medicine_generic = medicines.generic
            i.pharmaceuticals = medicines.pharmaceuticals
            data.append(i)
        return all_single_invoice

pharmacy_single_invoice_service = PhamrmacySingleInvoiceService(PharmacySingleInvoice, pharmacy_single_invoice_repo)