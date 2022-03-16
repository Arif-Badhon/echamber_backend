from repositories import BaseRepo
from models import DoctorSpeciality
from schemas import DoctorSpecialityIn, DoctorSpecialityOut
from sqlalchemy.orm import Session


class SpecialitiesRepo(BaseRepo[DoctorSpeciality, DoctorSpecialityIn, DoctorSpecialityOut]):
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.user_id == user_id).first()


doctor_specialities_repo = SpecialitiesRepo(DoctorSpeciality)
