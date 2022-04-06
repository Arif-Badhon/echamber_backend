from operator import or_
from repositories import BaseRepo
from models import EpMedicineList
from schemas import MedicineIn, MedicineUpdate
from sqlalchemy.orm import Session


class EpMedicineListRepo(BaseRepo[EpMedicineList, MedicineIn, MedicineUpdate]):
    def search_medicine(self, db: Session, search_medicine: str, skip: int = 0, limit: int = 10):
        query = db.query(self.model).filter(or_(
            self.model.name.like(f"%{search_medicine}%"),
            self.model.generic.like(f"%{search_medicine}%")
        )).offset(skip).limit(limit).all()

        return query


ep_medicines_list_repo = EpMedicineListRepo(EpMedicineList)
