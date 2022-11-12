from repositories import BaseRepo
from models import PharmaceuticalsNameList
from schemas import PharmaceuticalNameListIn, PharmaceuticalNameListUpdate
from sqlalchemy.orm import Session


class PharmaceuticalsNameListRepo(BaseRepo[PharmaceuticalsNameList, PharmaceuticalNameListIn, PharmaceuticalNameListUpdate]):

    def all_pharmaceuticals(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model).order_by(self.model.name).all()
        data = db.query(self.model).order_by(self.model.name).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def search_pharmaceuticals(self, db: Session, pharmaceuticals: str):
        data = db.query(self.model).filter(self.model.name.like(f"{pharmaceuticals}%")).all()
        return data

pharmaceuticals_name_list_repo = PharmaceuticalsNameListRepo(PharmaceuticalsNameList)