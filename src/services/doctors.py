from schemas import DoctorIn, DoctorUpdate, UserCreate
from models import Doctor
from schemas import DoctorSignup, DoctorQualilficationIn
from schemas.doctor_specialities import DoctorSpecialityIn
from services import BaseService, users_service
from services.doctor_qualifications import doctor_qualifications_service
from services.doctor_specialities import doctor_specialities_service
from repositories import doctors_repo
from sqlalchemy.orm import Session
from utils import ServiceResult, AppException, handle_result
from fastapi import status


class DoctorService(BaseService[Doctor, DoctorIn, DoctorUpdate]):

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

        if not specialities_user:
            return ServiceResult(AppException.ServerError(
                "Problem with Doctor registration."))
        else:

            return ServiceResult(handle_result(specialities_user), status_code=status.HTTP_201_CREATED)


doctors_service = DoctorService(Doctor, doctors_repo)
