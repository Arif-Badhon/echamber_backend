from repositories import BaseRepo
from models import PharmacyEverySingleStock, PharmacyTotalCurrentStock
from schemas import PharmacyEverySingleStockIn, PharmacyEverySingleStockUpdate
from sqlalchemy.orm import Session
from datetime import date, timedelta

class PharmacyEverySingleStockRepo(BaseRepo[PharmacyEverySingleStock, PharmacyEverySingleStockIn, PharmacyEverySingleStockUpdate]):
    def get_expired_medicine(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(PharmacyTotalCurrentStock.pharmacy_id == pharmacy_id).join(PharmacyTotalCurrentStock, PharmacyTotalCurrentStock.medicine_id == self.model.medicine_id).filter(self.model.expiry_date <= date.today()).all()
        data = db.query(self.model).filter(PharmacyTotalCurrentStock.pharmacy_id == pharmacy_id).join(PharmacyTotalCurrentStock, PharmacyTotalCurrentStock.medicine_id == self.model.medicine_id).filter(self.model.expiry_date <= date.today()).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]


    def get_nearly_expired_medicine(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(PharmacyTotalCurrentStock.pharmacy_id == pharmacy_id).join(PharmacyTotalCurrentStock, PharmacyTotalCurrentStock.medicine_id == self.model.medicine_id).filter(self.model.expiry_date >= date.today()).filter(self.model.expiry_date < (date.today() + timedelta(days=30))).all()
        data = db.query(self.model).filter(PharmacyTotalCurrentStock.pharmacy_id == pharmacy_id).join(PharmacyTotalCurrentStock, PharmacyTotalCurrentStock.medicine_id == self.model.medicine_id).filter(self.model.expiry_date >= date.today()).filter(self.model.expiry_date < (date.today() + timedelta(days=30))).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

pharmacy_every_single_stock_repo = PharmacyEverySingleStockRepo(PharmacyEverySingleStock)