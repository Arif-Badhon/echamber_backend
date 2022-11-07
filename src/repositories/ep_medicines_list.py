from operator import and_, or_
from repositories import BaseRepo
from models import EpMedicineList
from schemas import MedicineIn, MedicineUpdate
from sqlalchemy.orm import Session
from sqlalchemy.sql import func


class EpMedicineListRepo(BaseRepo[EpMedicineList, MedicineIn, MedicineUpdate]):
    def search_medicine(self, db: Session, search_medicine: str, skip: int = 0, limit: int = 10):
        data = []
        brand = db.query(self.model).filter(self.model.name.like(f"{search_medicine}%")).filter(or_(self.model.add_status != 'pending', self.model.add_status == None)).offset(skip).limit(limit).all()
        generic = db.query(self.model).filter(self.model.generic.like(f"{search_medicine}%")).filter(
            or_(self.model.add_status != 'pending', self.model.add_status == None)).offset(skip).limit(limit).all()
        data.extend(brand)
        data.extend(generic)

        return data

    def all_pharma(self, db: Session, skip: int, limit: int):
        data = db.query(func.distinct(self.model.pharmaceuticals)).order_by(self.model.pharmaceuticals).offset(skip).limit(limit).all()
        newdata = []
        for i in data:
            newdata.append({'pharmaceuticals': i[0]})
        return newdata

    def search_pharma(self, db: Session, pharma: str):
        data = db.query(func.distinct(self.model.pharmaceuticals)).filter(self.model.pharmaceuticals.like(f"{pharma}%")).all()
        newdata = []
        for i in data:
            newdata.append({'pharmaceuticals': i[0]})
        return newdata


ep_medicines_list_repo = EpMedicineListRepo(EpMedicineList)
