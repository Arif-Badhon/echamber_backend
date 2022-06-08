from repositories import BaseRepo
from models import EpChiefComplaintsList
from schemas import CcIn, CcUpdate
from sqlalchemy.orm import Session


class EpCcListRepo(BaseRepo[EpChiefComplaintsList, CcIn, CcUpdate]):

    def search_by_cc(self, db: Session, search_str: str, skip: int = 0, limit: int = 10):
        query = db.query(self.model).filter(
            self.model.chief_complaints.like(f"%{search_str}%")).offset(skip).limit(limit).all()
        return query


ep_chief_complaints_list_repo = EpCcListRepo(EpChiefComplaintsList)
