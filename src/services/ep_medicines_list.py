from sqlalchemy.orm import Session
from services import BaseService
from models import EpMedicineList
from schemas import MedicineIn, MedicineUpdate
from repositories import ep_medicines_list_repo
from fastapi import status
from exceptions import ServiceResult


class EpMedicineListService(BaseService[EpMedicineList, MedicineIn, MedicineUpdate]):
    def search_medicine(self, db: Session, search_medicine: str,  skip: int, limit: int):
        med = self.repo.search_medicine(
            db, search_medicine, skip, limit)
        if not med:
            return ServiceResult(med, status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(med, status_code=status.HTTP_200_OK)

    def all_pharma(self, db: Session, skip: int, limit: int):
        data = self.repo.all_pharma(db=db, skip=skip, limit=limit)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def search_pharma(self, db: Session, pharma: str):
        data = self.repo.search_pharma(db=db, pharma=pharma)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)


ep_medicine_list_service = EpMedicineListService(
    EpMedicineList, ep_medicines_list_repo)
