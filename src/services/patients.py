from exceptions.app_exceptions import AppException
from exceptions.service_result import ServiceResult, handle_result
from repositories import patients_repo
from services import users_service, user_details_service
from models import Patient
from schemas import PatientIn, PatientUpdate, UserCreate, UserDetailIn
from services import BaseService, UpdateSchemaType
from sqlalchemy.orm import Session
from services import CreateSchemaType, users_service
from fastapi import status


class PatientService(BaseService[Patient, PatientIn, PatientUpdate]):
    def get_by_user_id(self, db: Session, user_id: int):
        patient_detail = self.repo.get_by_user_id(db, user_id)
        if not patient_detail:
            return ServiceResult(AppException.NotFound("Patient not found"))
        else:
            return ServiceResult(patient_detail, status_code=status.HTTP_200_OK)
    
    def search_by_patient_name(self, db: Session, name: str, skip:int, limit: int):
        patients = self.repo.search_by_patient_name(db=db, name=name, skip=skip, limit=limit)

        data = []

        for i in patients:
            detail = user_details_service.get_by_user_id(db=db, id=i.id)
            if not detail:
                i.dob = None
                i.division = None 
                # i.blood_group = None
            else:
                i.dob = handle_result(detail).dob
                i.division = handle_result(detail).division
                i.blood_group = handle_result(detail).blood_group
            data.append(i)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)

    def update_by_user_id(self, db: Session, user_id: int, data_update: UpdateSchemaType):
        exist = self.repo.get_by_user_id(db, user_id)
        if not exist:
            new_data = PatientIn(
                user_id=user_id,
                bio=data_update.bio,
                marital_status=data_update.marital_status,
                occupation=data_update.occupation
            )
            self.create(db, data_in=new_data)
            check = self.repo.get_by_user_id(db, user_id)
            return ServiceResult(check, status_code=status.HTTP_202_ACCEPTED)
        else:
            data = self.repo.update_by_user_id(db, user_id, data_update)
            if not data:
                return ServiceResult(AppException.NotAccepted())
            return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)

    def signup(self, db: Session, data_in: CreateSchemaType):

        singnup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name='patient'
        )

        signup_user = users_service.signup(
            db, data_in=singnup_data, flush=True)

        user_details_data = UserDetailIn(
            user_id=handle_result(signup_user).id,
            country=data_in.country,
            division=data_in.division,
            district=data_in.district,
            sub_district=data_in.sub_district,
            post_code=data_in.post_code,
            dob=data_in.dob
        )

        ud = user_details_service.create(db, data_in=user_details_data)

        if not ud:
            return ServiceResult(AppException.ServerError(
                "Problem with patient registration."))
        else:
            return ServiceResult(handle_result(ud), status_code=status.HTTP_201_CREATED)


patients_service = PatientService(Patient, patients_repo)
