from sqlalchemy.orm import Session
from services import BaseService
from repositories import doctor_chambers_repo, ModelType
from models import DoctorChamber
from schemas import DoctorChamberIn, DoctorChamberUpdate
from exceptions import ServiceResult, AppException
from fastapi import status


class DoctorChamberService(BaseService[DoctorChamber, DoctorChamberIn, DoctorChamberUpdate]):

    def create_with_user_id(self, db: Session, data_in: DoctorChamberIn, user_id: int):
        chamber_in = self.repo.create_with_user_id(db, data_in, user_id)
        if not chamber_in:
            return ServiceResult(AppException.NotFound("Something went wrong!"))
        else:
            return ServiceResult(chamber_in, status_code=status.HTTP_200_OK)

    def active_chamber(self, db: Session, id: int, user_id: int):
        # exception needed
        deactivate = doctor_chambers_repo.chamber_deactive_by_user_id(
            db, user_id=user_id)

        active = doctor_chambers_repo.chamber_active_by_id(db, id=id)

        return self.get_by_user_id(db, user_id)

    def currently_active_chamber(self, db: Session, user_id: int):
        active = self.repo.currently_active_chamber(db=db, user_id=user_id)
        if not active:
            return ServiceResult(AppException.NotFound("No chamber active or something went wrong."))
        else:
            return ServiceResult(active, status_code=status.HTTP_200_OK)


doctor_chambers_service = DoctorChamberService(
    DoctorChamber, doctor_chambers_repo)
