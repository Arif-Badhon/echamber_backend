from services import BaseService, ModelType
from models import DoctorQualification
from schemas import DoctorQualilficationIn, DoctorQualilficationUpdate
from repositories import doctor_qualifications_repo
from sqlalchemy.orm import Session
from utils import ServiceResult, AppException
from fastapi import status


class QualificationService(BaseService[DoctorQualification, DoctorQualilficationIn, DoctorQualilficationUpdate]):
    def get_by_user_id(self, db: Session, user_id: int) -> ModelType:
        patient_detail = self.repo.get_by_user_id(db, user_id)
        if not patient_detail:
            return ServiceResult(AppException.NotFound("Qualification not found"))
        else:
            return ServiceResult(patient_detail, status_code=status.HTTP_200_OK)

    def create_with_flush(self, db: Session, data_in: DoctorQualilficationIn):
        data = self.repo.create_with_flush(db, data_in)

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)


doctor_qualifications_service = QualificationService(
    DoctorQualification, doctor_qualifications_repo)
