from repositories import BaseRepo, roles_repo
from models import ClinicActivity, User
from schemas import ClinicActivityIn, ClinicActivityUpdate
from sqlalchemy.orm import Session

class ClinicActivityRepo(BaseRepo[ClinicActivity, ClinicActivityIn, ClinicActivityUpdate]):
    
    def get_activity_by_clinic_id(self, db: Session, clinic_id: int, skip: int, limit: int):
        data_count =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        data =  db.query(self.model).filter(self.model.clinic_id == clinic_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]


    def get_clinic_patient(self, db: Session, clinic_id: int, skip: int, limit: int):

        role_id = roles_repo.search_name_id(db=db, name='patient')
        print(role_id)

        data_count = db.query(self.model, User).join(self.model, self.model.service_received_id == User.id).filter(User.role_id == role_id).filter(self.model.clinic_id == clinic_id).all()
        data = db.query(self.model, User).join(self.model, self.model.service_received_id == User.id).filter(User.role_id == role_id).filter(self.model.clinic_id == clinic_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

clinic_activity_repo = ClinicActivityRepo(ClinicActivity)