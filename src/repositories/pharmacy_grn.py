from repositories import BaseRepo
from models import PharmacyGrn
from schemas import PharmacyGrnIn, PharmacyGrnUpdate
from sqlalchemy.orm import Session


class PharmacyGrnRepo(BaseRepo[PharmacyGrn, PharmacyGrnIn, PharmacyGrnUpdate]):
    def get_grn_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).all()
        data =  db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

pharmacy_grn_repo = PharmacyGrnRepo(PharmacyGrn)