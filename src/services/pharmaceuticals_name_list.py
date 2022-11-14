from services import BaseService
from models import PharmaceuticalsNameList
from schemas import PharmaceuticalNameListIn, PharmaceuticalNameListUpdate
from repositories import pharmaceuticals_name_list_repo
from exceptions import ServiceResult
from sqlalchemy.orm import Session
from fastapi import status


class PharmaceuticalsNameListService(BaseService[PharmaceuticalsNameList, PharmaceuticalNameListIn, PharmaceuticalNameListUpdate]):
    def all_pharmaceuticals(self, db: Session, skip: int, limit: int):
        data = self.repo.all_pharmaceuticals(db=db, skip=skip, limit=limit)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def search_pharmaceuticals(self, db: Session, pharmaceuticals: str):
        data = self.repo.search_pharmaceuticals(db=db, pharmaceuticals=pharmaceuticals)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

pharmaceuticals_name_list_service = PharmaceuticalsNameListService(PharmaceuticalsNameList, pharmaceuticals_name_list_repo)