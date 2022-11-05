from repositories import BaseRepo
from models import ClinicWithDoctor, User
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate
from sqlalchemy.orm import Session


class ClinicWithDoctorRepo(BaseRepo[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate]):
    
    def search_by_clinic_id(self, db: Session, clinic_id: int):
        return db.query(self.model, User).join(self.model, self.model.doctor_id ==  User.id).filter(self.model.clinic_id == clinic_id).all()

clinic_with_doctor_repo = ClinicWithDoctorRepo(ClinicWithDoctor)