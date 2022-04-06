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


ep_medicine_list_service = EpMedicineListService(
    EpMedicineList, ep_medicines_list_repo)
