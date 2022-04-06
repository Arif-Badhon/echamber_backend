from exceptions import ServiceResult, AppException
from services import BaseService
from repositories import ep_investigations_list_repo
from models import EpInvestigationList
from schemas import InvIn, InvUpdate
from sqlalchemy.orm import Session
from fastapi import status


class EpInvListService(BaseService[EpInvestigationList, InvIn, InvUpdate]):
    def search_by_inv(self, db: Session, search_str: str, skip: int, limit: int):
        inv = self.repo.search_by_inv(db, search_str, skip, limit)
        if not inv:
            return ServiceResult(inv, status_code=status.HTTP_200_OK)
            # return ServiceResult(AppException.NotFound("Result not found"))
        else:
            return ServiceResult(inv, status_code=status.HTTP_200_OK)


ep_investigations_list_service = EpInvListService(
    EpInvestigationList, ep_investigations_list_repo)
