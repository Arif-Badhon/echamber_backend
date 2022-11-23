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

    def invoice_filter(self, db: Session, pharmacy_id: int, customer_id: int, start_date: str, end_date: str, single_date: str, skip: int, limit: int):
        
        if start_date is None:
            start_date = ''
        if single_date is None:
            single_date = ''

        print(customer_id)
        
        if customer_id is not None:
            data_count = db.query(self.model).filter(self.model.customer_id == customer_id).filter(self.model.pharmacy_id == pharmacy_id).all()
            data = db.query(self.model).filter(self.model.customer_id == customer_id).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
            return [{"results": len(data_count)}, data]
        elif len(start_date) !=0 :
            data_count = db.query(self.model).filter(self.model.created_at.between(start_date, end_date)).filter(self.model.pharmacy_id == pharmacy_id).all()
            data = db.query(self.model).filter(self.model.created_at.between(start_date, end_date)).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
            return [{"results": len(data_count)}, data]
        elif len(single_date) != 0:
            data_count = db.query(self.model).filter(self.model.created_at.like(f"%{single_date}%")).filter(self.model.pharmacy_id == pharmacy_id).all()
            data = db.query(self.model).filter(self.model.created_at.like(f"%{single_date}%")).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
            return [{"results": len(data_count)}, data]
        else:
            data_count =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).all()
            data =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
            return [{"results": len(data_count)}, data]



    def get_total_sale(self, db: Session, pharmacy_id: int, customer_id: int, start_date: str, end_date: str):

        if customer_id is not None:
            data = db.query(func.sum(self.model.paid_amount)).filter(self.model.pharmacy_id == pharmacy_id).filter(self.model.customer_id == customer_id).all()
            return data[0][0]

        if start_date is not None:
            data = db.query(func.sum(self.model.paid_amount)).filter(self.model.pharmacy_id == pharmacy_id).filter(self.model.created_at.between(start_date, end_date)).all()
            return data[0][0]

pharmacy_invoice_repo = PhamracyInvoiceRepo(PharmacyInvoice)
