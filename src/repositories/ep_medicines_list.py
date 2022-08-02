from operator import and_, or_
from repositories import BaseRepo
from models import EpMedicineList
from schemas import MedicineIn, MedicineUpdate
from sqlalchemy.orm import Session


class EpMedicineListRepo(BaseRepo[EpMedicineList, MedicineIn, MedicineUpdate]):
    def search_medicine(self, db: Session, search_medicine: str, skip: int = 0, limit: int = 10):
        data = []
        brand = db.query(self.model).filter(self.model.name.like(f"%{search_medicine}")).offset(skip).limit(limit).all()
        generic = db.query(self.model).filter(self.model.generic.like(f"%{search_medicine}")).offset(skip).limit(limit).all()
        data.extend(brand)
        data.extend(generic)
        return data


ep_medicines_list_repo = EpMedicineListRepo(EpMedicineList)
