from services import BaseService
from models import EpAdviceList
from schemas import AdviceIn, AdviceUpdate
from repositories import ep_advices_list_repo
from sqlalchemy.orm import Session
from fastapi import status
from exceptions import ServiceResult


class EpAdviceListService(BaseService[EpAdviceList, AdviceIn, AdviceUpdate]):
    def search_by_advice(self, db: Session, search_str: str, skip: int, limit: int):
        adv = self.repo.search_by_advice(db, search_str, skip, limit)
        if not adv:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(adv, status_code=status.HTTP_200_OK)


ep_advices_list_service = EpAdviceListService(
    EpAdviceList, ep_advices_list_repo)
