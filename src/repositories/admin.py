from sqlalchemy import desc
from sqlalchemy.orm import Session
from repositories import BaseRepo
from .roles import roles_repo
from .pharmacy import pharmacy_repo
from .clinic import clinic_repo
from schemas import UserCreate, UserUpdate, PharmacyUpdate, ClinicUpdate
from models import User, Doctor, DoctorQualification, DoctorSpeciality, DoctorChamber, DoctorWorkPlace, AdminPanelActivity, Pharmacy, Clinic


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()

    def all_employee(self, db: Session, skip: int = 0, limit: int = 10, is_active: bool = True):
        all_employee_role = [1, 2, 5, 6, 7]

        query = db.query(self.model).filter(self.model.role_id.in_(all_employee_role)).filter(self.model.is_active == is_active).offset(skip).limit(limit).all()
        query_all = db.query(self.model).filter(self.model.role_id.in_(all_employee_role)).filter(self.model.is_active == is_active).all()

        return [{"results": len(query_all)}, query]

    def user_active_switcher(self, db: Session, id: int):
        current_status = self.get_one(db=db, id=id).is_active
        data = self.update(db=db, id=id, data_update=UserUpdate(is_active=not current_status))
        return data


    # all doctor repo

    def doctors_active_list(self, db: Session, name: str, phone: str, speciality: str, district: str, bmdc: str, start_date: str, end_date: str,  skip: int = 0, limit: int = 10):

        # for all result
        if name is None:
            name = ''
        if speciality is None:
            speciality = ''
        if district is None:
            district = ''
        if phone is None:
            phone = ''
        if bmdc is None:
            bmdc = ''

        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.created_at.between(start_date, end_date)).filter(
            User.name.like(f"%{name}%")).filter(
            User.phone.like(f"%{phone}%")).filter(
            DoctorSpeciality.speciality.like(f"%{speciality}%")).filter(
            Doctor.bmdc.like(f"%{bmdc}%")).offset(skip).limit(limit).all()
        query_all = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.created_at.between(start_date, end_date)).filter(
            User.name.like(f"%{name}%")).filter(
            User.phone.like(f"%{phone}%")).filter(
            DoctorSpeciality.speciality.like(f"%{speciality}%")).filter(
            Doctor.bmdc.like(f"%{bmdc}%")).all()
        results = len(query_all)
        return [{"results": results}, query]
    
    # antor
    def doctors_active_list_with_area(self, db: Session, name: str, speciality: str, district: str, start_date: str, end_date: str, skip: int = 0, limit: int = 10):

        # for all result
        if name is None:
            name = ''
        if speciality is None:
            speciality = ''
        if district is None:
            district = ''

        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.id == DoctorChamber.user_id).filter(
            User.created_at.between(start_date, end_date)).filter(
            User.name.like(f"%{name}%")).filter(
            DoctorSpeciality.speciality.like(f"%{speciality}%")).filter(
            DoctorChamber.district.like(f"%{district}%")).offset(skip).limit(limit).all()
        query_all = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == True).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.id == DoctorChamber.user_id).filter(
            User.created_at.between(start_date, end_date)).filter(
            User.name.like(f"%{name}%")).filter(
            DoctorSpeciality.speciality.like(f"%{speciality}%")).filter(
            DoctorChamber.district.like(f"%{district}%")).all()
        results = len(query_all)
        return [{"results": results}, query]

    def doctors_inactive_list(self, db: Session, start_date: str, end_date: str, skip: int = 0, limit: int = 10):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == False).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.created_at.between(start_date, end_date)).offset(skip).limit(limit).all()
        query_all = db.query(
            User, Doctor, DoctorQualification, DoctorSpeciality).join(Doctor).filter(
            User.role_id == doctor_role_id).order_by(
            desc(self.model.created_at)).filter(
            User.is_active == False).filter(
            User.id == DoctorQualification.user_id).filter(
            User.id == DoctorSpeciality.user_id).filter(
            User.created_at.between(start_date, end_date)).all()
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

    def all_patient(self, db: Session, start_date: str, end_date: str, phone_number: str = "0",  skip: int = 0, limit: int = 15):

        # for all result
        if phone_number is None:
            phone_number = ''

        patient_role = roles_repo.search_name_id(db=db, name='patient')
        query = db.query(
            self.model).filter(
            self.model.role_id == patient_role).filter(
            User.created_at.between(start_date, end_date)).order_by(
            desc(self.model.created_at)).filter(
            self.model.phone.like(f"%{phone_number}%")).offset(skip).limit(limit).all()
        query_all = db.query(
            self.model).filter(
            self.model.role_id == patient_role).filter(
            User.created_at.between(start_date, end_date)).order_by(
            desc(self.model.created_at)).filter(
            self.model.phone.like(f"%{phone_number}%")).all()

        results = len(query_all)

        return [{"results": results}, query]

    def all_patient_filter(self, db: Session,  hx_user_id: int, name: str, phone: str, gender: str, start_date: str, end_date: str,  skip: int, limit: int):

        if name is None:
            name = ''
        if phone is None:
            phone = ''
        if gender is None:
            gender = ''

        if hx_user_id is not None:
            query_len = len(db.query(self.model).filter(self.model.id == hx_user_id).filter(self.model.is_active == True).all())
            query = db.query(self.model).filter(self.model.id == hx_user_id).filter(self.model.is_active == True).offset(skip).limit(limit).all()
            return [{"results": query_len}, query]
        else:
            query_len = len(db.query(
                self.model).filter(
                self.model.is_active == True).filter(
                self.model.name.like(f"%{name}%")).filter(
                self.model.phone.like(f"%{phone}%")).filter(
                self.model.sex.like(f"{gender}%")).filter(
                User.created_at.between(start_date, end_date)).all())
            query = db.query(
                self.model).filter(
                self.model.is_active == True).filter(
                self.model.name.like(f"%{name}%")).filter(
                self.model.phone.like(f"%{phone}%")).filter(
                self.model.sex.like(f"{gender}%")).filter(
                User.created_at.between(start_date, end_date)).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
            return [{"results": query_len}, query]

    # Pharmacy

    def pharmacy_active_list(self, db: Session, skip: int, limit: int):
        data_count = db.query(Pharmacy).filter(Pharmacy.pharmacy_is_active == True).all()
        data = db.query(Pharmacy).filter(Pharmacy.pharmacy_is_active == True).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def pharmacy_inactive_list(self, db: Session, skip: int, limit: int):
        data_count = db.query(Pharmacy).filter(Pharmacy.pharmacy_is_active == False).all()
        data = db.query(Pharmacy).filter(Pharmacy.pharmacy_is_active == False).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def pharmacy_active_switcher(self, db: Session, id: int):
        current_status = pharmacy_repo.get_one(db=db, id=id).pharmacy_is_active
        data = pharmacy_repo.update(db=db, id=id, data_update=PharmacyUpdate(pharmacy_is_active=not current_status))
        return data

    # Clinic

    def clinic_active_list(self, db: Session, skip: int, limit: int):
        data_count = db.query(Clinic).filter(Clinic.clinic_is_active == True).all()
        data = db.query(Clinic).filter(Clinic.clinic_is_active == True).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def clinic_inactive_list(self, db: Session, skip: int, limit: int):
        data_count = db.query(Clinic).filter(Clinic.clinic_is_active == False).all()
        data = db.query(Clinic).filter(Clinic.clinic_is_active == False).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def clinic_active_switcher(self, db: Session, id: int):
        current_status = clinic_repo.get_one(db=db, id=id).clinic_is_active
        data = clinic_repo.update(db=db, id=id, data_update=ClinicUpdate(clinic_is_active=not current_status))
        return data


admin_repo = AdminRepo(User)
