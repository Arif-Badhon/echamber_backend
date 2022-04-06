from exceptions import ServiceResult, AppException
from services import BaseService
from repositories import ep_chief_complaints_list_repo
from models import EpChiefComplaintsList
from schemas import CcIn, CcUpdate
from sqlalchemy.orm import Session
from fastapi import status


class EpCcListService(BaseService[EpChiefComplaintsList, CcIn, CcUpdate]):
    def search_by_cc(self, db: Session, search_str: str, skip: int, limit: int):
        cc = self.repo.search_by_cc(db, search_str, skip, limit)
        if not cc:
            return ServiceResult(cc, status_code=status.HTTP_200_OK)
            # return ServiceResult(AppException.NotFound("Result not found"))
        else:
            return ServiceResult(cc, status_code=status.HTTP_200_OK)


ep_chief_complaints_list_service = EpCcListService(
    EpChiefComplaintsList, ep_chief_complaints_list_repo)
