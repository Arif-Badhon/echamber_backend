from repositories import BaseRepo
from models import Pharmaceuticals, PharmaceuticalsNameList
from schemas import PharmaceuticalIn, PharmaceuticalUpdate
from sqlalchemy.orm import Session

class PharmaceuticalsRepo(BaseRepo[Pharmaceuticals, PharmaceuticalIn, PharmaceuticalUpdate]):

    def all_pharmaceuticals(self, db: Session, skip: int, limit: int):
        data = db.query(PharmaceuticalsNameList).order_by(PharmaceuticalsNameList.name).offset(skip).limit(limit).all()
        return data

    def search_pharmaceuticals(self, db: Session, pharmaceuticals: str):
        data = db.query(PharmaceuticalsNameList).filter(PharmaceuticalsNameList.name.like(f"{pharmaceuticals}%")).all()
        return data

pharmaceuticals_repo = PharmaceuticalsRepo(Pharmaceuticals)
