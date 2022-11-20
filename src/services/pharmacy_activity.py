from services import BaseService
from models import PharmacyActivity
from schemas import PharmacyActivityIn, PharmacyActivityUpdate
from repositories import pharmacy_activity_repo
from sqlalchemy.orm import Session


class PharmacyActivityService(BaseService[PharmacyActivity, PharmacyActivityIn, PharmacyActivityUpdate]):

    def get_activity_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        get_activity = self.repo.get_activity_by_pharmacy_id(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
        return get_activity

    def get_pharmacy_patient(self, db: Session, pharmacy_id: int, skip: int, limit:int):
        get_patient = self.repo.get_pharmacy_patient(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
        return get_patient

pharmacy_activity_service = PharmacyActivityService(PharmacyActivity, pharmacy_activity_repo)
