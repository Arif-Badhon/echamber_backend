from services import BaseService, ModelType
from models import DoctorSpeciality
from schemas import DoctorSpecialityIn, DoctorQualilficationUpdate
from repositories import doctor_specialities_repo
from fastapi import status
from sqlalchemy.orm import Session
from utils import ServiceResult, AppException


class SpecialitiesService(BaseService[DoctorSpeciality, DoctorSpecialityIn, DoctorQualilficationUpdate]):
    def get_by_user_id(self, db: Session, user_id: int) -> ModelType:
        patient_detail = self.repo.get_by_user_id(db, user_id)
        if not patient_detail:
            return ServiceResult(AppException.NotFound("Specialities not found"))
        else:
            return ServiceResult(patient_detail, status_code=status.HTTP_200_OK)

    def create_with_flush(self, db: Session, data_in: DoctorSpecialityIn):
        data = self.repo.create_with_flush(db, data_in)

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)


doctor_specialities_service = SpecialitiesService(
    DoctorSpeciality, doctor_specialities_repo)
