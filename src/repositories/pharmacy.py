from repositories import BaseRepo
from models import Pharmacy
from schemas import PharmacyIn, PharmacyUpdate
from sqlalchemy.orm import Session

class PharmacyRepo(BaseRepo[Pharmacy, PharmacyIn, PharmacyUpdate]):
    def search_by_trade_license(self, db: Session, trade_license: str):
        query = db.query(self.model).filter(self.model.trade_license == trade_license).first()
        return query

pharmacy_repo = PharmacyRepo(Pharmacy)