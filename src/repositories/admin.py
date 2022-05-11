from sqlalchemy import or_
from sqlalchemy.orm import Session
from repositories import BaseRepo
from .roles import roles_repo
from schemas import UserCreate, UserUpdate
from models import User, Doctor, DoctorQualification, DoctorSpeciality


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()

    def all_employee(self, db: Session, skip: int = 0, limit: int = 10):
        doctor_id = roles_repo.search_name_id(db, name='doctor')
        patient_id = roles_repo.search_name_id(db, name='patient')
        query = db.query(self.model).filter(self.model.role_id != doctor_id).filter(self.model.role_id != patient_id).offset(skip).limit(limit).all()
        return query

    def doctors_active_list(self, db: Session):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(User, Doctor,DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).filter(User.is_active == True).filter(User.id == DoctorQualification.user_id).filter(User.id==DoctorSpeciality.user_id).all()
        return query



    def doctors_inactive_list(self, db: Session):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(User, Doctor,DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).filter(User.is_active == False).filter(User.id == DoctorQualification.user_id).filter(User.id==DoctorSpeciality.user_id).all()
        return query
    


    def doctor_active_by_id(self, db: Session, id):
        db.query(self.model).filter(self.model.id == id).update(
            {self.model.is_active: True}, synchronize_session=False)
        db.commit()
        return self.get_one(db, id)


admin_repo = AdminRepo(User)
