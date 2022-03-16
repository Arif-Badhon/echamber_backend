from models import DoctorQualification
from schemas import DoctorQualilficationIn, DoctorQualilficationUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session


class QualificationRepo(BaseRepo[DoctorQualification, DoctorQualilficationIn, DoctorQualilficationUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        return db.query(self.model).filter(self.model.user_id == user_id).first()


doctor_qualifications_repo = QualificationRepo(DoctorQualification)
