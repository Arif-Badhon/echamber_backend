from sqlalchemy import desc
from sqlalchemy.orm import Session
from repositories import BaseRepo
from .roles import roles_repo
from schemas import UserCreate, UserUpdate
from models import User, Doctor, DoctorQualification, DoctorSpeciality, AdminPanelActivity


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()

    def all_employee(self, db: Session, skip: int = 0, limit: int = 10, is_active: bool = True):
        doctor_id = roles_repo.search_name_id(db, name='doctor')
        patient_id = roles_repo.search_name_id(db, name='patient')

        query = db.query(self.model).filter(self.model.role_id != doctor_id).filter(self.model.role_id != patient_id).filter(self.model.is_active == is_active).offset(skip).limit(limit).all()
        query_all = db.query(self.model).filter(self.model.role_id != doctor_id).filter(self.model.role_id != patient_id).filter(self.model.is_active == is_active).all()

        return [{"results": len(query_all)}, query]

    def user_active_switcher(self, db: Session, id: int):
        current_status = self.get_one(db=db, id=id).is_active
        data = self.update(db=db, id=id, data_update=UserUpdate(is_active=not current_status))
        return data

    # all doctor repo

    def doctors_active_list(self, db: Session, skip: int = 0, limit: int = 10):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).offset(skip).limit(limit).all()
        query_all = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).all()
        results = len(query_all)
        return [{"results": results}, query]

    def doctors_inactive_list(self, db: Session, skip: int = 0, limit: int = 10):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == False).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).offset(skip).limit(limit).all()
        query_all = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == False).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).all()
        results = len(query_all)
        return [{"results": results}, query]

    def doctor_active_by_id(self, db: Session, id):
        db.query(self.model).filter(self.model.id == id).update(
            {self.model.is_active: True}, synchronize_session=False)
        db.commit()
        return self.get_one(db, id)

    # all patient repo

    def patient_register_by_whom(self, db: Session, patient_id: int):
        """ This method reveal who registered a patient """
        query = db.query(AdminPanelActivity).filter(AdminPanelActivity.service_name == 'patient_register').filter(AdminPanelActivity.service_recived_id == patient_id).first()
        return query

    def all_patient(self, db: Session, phone_number: str = "0", skip: int = 0, limit: int = 15):

        # for all result
        if phone_number is None:
            phone_number = ''

        patient_role = roles_repo.search_name_id(db=db, name='patient')
        query = db.query(self.model).filter(self.model.role_id == patient_role).order_by(desc(self.model.created_at)).filter(self.model.phone.like(f"%{phone_number}%")).offset(skip).limit(limit).all()
        query_all = db.query(self.model).filter(self.model.role_id == patient_role).order_by(desc(self.model.created_at)).filter(self.model.phone.like(f"%{phone_number}%")).all()

        results = len(query_all)

        return [{"results": results}, query]

    def all_patient_filter(self):
        return


admin_repo = AdminRepo(User)
