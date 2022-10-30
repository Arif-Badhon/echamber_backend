from schemas import DoctorIn, DoctorUpdate, UserCreate
from models import Doctor
from schemas import DoctorSignup, DoctorQualilficationIn, DoctorUpdate
from schemas.doctor_specialities import DoctorSpecialityIn
from services import BaseService
from .users import users_service
from .roles import roles_service
from services.doctor_qualifications import doctor_qualifications_service
from services.doctor_specialities import doctor_specialities_service
from repositories import doctors_repo, users_repo, roles_repo
from sqlalchemy.orm import Session
from utils import ServiceResult, AppException, handle_result
from fastapi import status


class DoctorService(BaseService[Doctor, DoctorIn, DoctorUpdate]):

    def get_by_user_id(self, db: Session, user_id: int):
        data = self.repo.get_by_user_id(db=db, user_id=user_id)
        if not data:
            return ServiceResult(AppException.ServerError("Not found"))
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def edit_by_user_id(self, db: Session, data_update: DoctorUpdate, user_id: int):
        doc = self.get_by_user_id(db=db, user_id=user_id)
        up = self.update(db=db, id=handle_result(doc).id, data_update=data_update)
        return up

    def create_with_flush(self, db: Session, data_in: DoctorIn):
        data = self.repo.create_with_flush(db, data_in)

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def signup(self, db: Session, data_in: DoctorSignup):

        sginup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=False,
            password=data_in.password,
            role_name='doctor'
        )

        signup_user = users_service.signup(db, data_in=sginup_data, flush=True)

        doctor_data = DoctorIn(
            user_id=handle_result(signup_user).id,
            bmdc=data_in.bmdc
        )

        doctor_user = self.create_with_flush(db, data_in=doctor_data)

        qualification_data = DoctorQualilficationIn(
            user_id=handle_result(signup_user).id,
            qualification=data_in.qualification
        )

        qualification_user = doctor_qualifications_service.create_with_flush(
            db, data_in=qualification_data)

        specialities_data = DoctorSpecialityIn(
            user_id=handle_result(signup_user).id,
            speciality=data_in.speciality
        )

        specialities_user = doctor_specialities_service.create(
            db, data_in=specialities_data)

        get_doctor = users_repo.get_one(db=db, id=handle_result(signup_user).id)
        print(get_doctor)

        if not get_doctor:
            return ServiceResult(AppException.ServerError(
                "Doctor not register perfectly."))
        else:
            return ServiceResult(get_doctor, status_code=status.HTTP_201_CREATED)

    def all_doc(self, db: Session, skip: int, limit: int):
        role_id = roles_service.role_id_by_name(db=db, name="doctor")
        docs = users_service.get_by_two_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, is_active=True, role_id=role_id)

        return docs

    def details(self, db: Session, id: int):
        user = users_service.get_one(db=db, id=id)
        role_id = handle_result(user).role_id
        role = roles_service.get_one(db=db, id=role_id)
        role_name = handle_result(role).name

        if role_name != 'doctor':
            return ServiceResult(AppException.ServerError("This user is not a doctor."))

        doctors = self.get_by_user_id(db=db, user_id=id)

        specialities = doctor_specialities_service.get_by_key(db=db, skip=0, limit=15, descending=False, count_results=False, user_id=id)

        qualifications = doctor_qualifications_service.get_by_key(db=db, skip=0, limit=15, descending=False, count_results=False, user_id=id)

        return {"user": handle_result(user), "doctor": handle_result(doctors), "specialities": handle_result(specialities), "qualifications": handle_result(qualifications)}
        # return {user, specialities, qualifications}


doctors_service = DoctorService(Doctor, doctors_repo)
