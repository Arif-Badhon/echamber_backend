from repositories.base import BaseRepo
from models import Doctor
from schemas import DoctorIn, DoctorUpdate
from sqlalchemy.orm import Session


class DoctorRepo(BaseRepo[Doctor, DoctorIn, DoctorUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.user_id == user_id).first()


doctors_repo = DoctorRepo(Doctor)
