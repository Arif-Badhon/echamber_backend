from repositories import BaseRepo
from models import PharmacyInvoice
from schemas import PharmacyInvoiceIn, PharmacyInvoiceUpdate
from sqlalchemy.orm import Session
from sqlalchemy.sql import func

class PhamracyInvoiceRepo(BaseRepo[PharmacyInvoice, PharmacyInvoiceIn, PharmacyInvoiceUpdate]):

    def get_invoice_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).all()
        data =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]



    def get_total_sale(self, db: Session, pharmacy_id: int):

        data = db.query(func.sum(self.model.customer_id)).filter(self.model.pharmacy_id == pharmacy_id).all()
        return data[0][0]

pharmacy_invoice_repo = PhamracyInvoiceRepo(PharmacyInvoice)
