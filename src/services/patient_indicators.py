from fastapi import status
from exceptions import ServiceResult, AppException
from repositories import patient_indicators_repo
from schemas.patient_indicators import PatientIndicatorBase
from services import BaseService, ModelType
from models import PatientIndicator
from schemas import PatientIndicatorIn, PatientIndicatorUpdate
from sqlalchemy.orm import Session


class PatientService(BaseService[PatientIndicator, PatientIndicatorIn, PatientIndicatorUpdate]):

    def create_by_user_id(self, db: Session, user_id: int, data_in: PatientIndicatorBase) -> ModelType:
        data = self.repo.create_by_user_id(db, user_id, data_in)

        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)

    def get_by_key(self, db: Session, key: str, user_id: int):
        data = self.repo.get_by_key(db, key, user_id)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def get_last_item(self, db: Session, key: str, user_id: int):
        data = self.repo.get_last_item(db, key, user_id)

        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_200_OK)


patient_indicators_service = PatientService(
    PatientIndicator, patient_indicators_repo)
