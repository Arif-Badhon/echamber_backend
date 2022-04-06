from repositories import BaseRepo
from models import EpInvestigationList
from schemas import InvIn, InvUpdate
from sqlalchemy.orm import Session


class EpInvListRepo(BaseRepo[EpInvestigationList, InvIn, InvUpdate]):
    def search_by_inv(self, db: Session, search_str: str, skip: int = 0, limit: int = 10):
        query = db.query(self.model).filter(
            self.model.investigation.like(f"%{search_str}%")).offset(skip).limit(limit).all()
        return query


ep_investigations_list_repo = EpInvListRepo(EpInvestigationList)
