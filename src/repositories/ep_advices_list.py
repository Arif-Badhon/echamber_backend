from repositories import BaseRepo
from models import EpAdviceList
from schemas import AdviceIn, AdviceUpdate
from sqlalchemy.orm import Session


class EpAdviceListRepo(BaseRepo[EpAdviceList, AdviceIn, AdviceUpdate]):
    def search_by_advice(self, db: Session, search_str: str, skip: int = 0, limit: int = 10):
        query = db.query(self.model).filter(
            self.model.advice.like(f"%{search_str}%")).offset(skip).limit(limit).all()
        return query


ep_advices_list_repo = EpAdviceListRepo(EpAdviceList)
