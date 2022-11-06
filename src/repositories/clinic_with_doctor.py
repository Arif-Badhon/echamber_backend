from repositories import BaseRepo
from models import ClinicWithDoctor, User, Doctor, DoctorQualification, DoctorSpeciality
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate
from sqlalchemy.orm import Session


class ClinicWithDoctorRepo(BaseRepo[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate]):
    
    def search_by_clinic_id(self, db: Session, clinic_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        data =  db.query(self.model, User, Doctor, DoctorQualification, DoctorSpeciality).join(self.model, self.model.doctor_id ==  User.id).filter(self.model.doctor_id == Doctor.user_id).filter(self.model.doctor_id == DoctorQualification.user_id).filter(self.model.doctor_id == DoctorSpeciality.user_id).filter(self.model.clinic_id == clinic_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

clinic_with_doctor_repo = ClinicWithDoctorRepo(ClinicWithDoctor)