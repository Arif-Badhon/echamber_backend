from services import BaseService
from models import ClinicActivity
from schemas import ClinicActivityIn, ClinicActivityUpdate
from repositories import clinic_activity_repo
from sqlalchemy.orm import Session


class ClinicActivityService(BaseService[ClinicActivity, ClinicActivityIn, ClinicActivityUpdate]):

    def get_activity_by_clinic_id(self, db: Session, clinic_id: int, skip: int, limit: int):
        get_activity = self.repo.get_activity_by_clinic_id(db=db, clinic_id=clinic_id, skip=skip, limit=limit)
        return get_activity

    def get_clinic_patient(self, db: Session, clinic_id: int, skip: int, limit:int):
        get_patient = self.repo.get_clinic_patient(db=db, clinic_id=clinic_id, skip=skip, limit=limit)
        return get_patient

clinic_activity_service = ClinicActivityService(ClinicActivity, clinic_activity_repo)
