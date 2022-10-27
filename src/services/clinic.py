from services import BaseService, users_service
from models import Clinic
from schemas import ClinicIn, ClinicUpdate, ClinicUserWithClinic, UserCreate, ClinicBase, ClinicUserIn, ClinicLogin
from repositories import clinic_repo, users_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result, ServiceResult
from .clinic_user import clinic_user_service
from exceptions.app_exceptions import AppException
from fastapi import status

class ClinicService(BaseService[Clinic, ClinicIn, ClinicUpdate]):
    

    def register_clinic(self, db: Session, data_in: ClinicUserWithClinic):
        admin_signup = UserCreate(
            name = data_in.user.name,
            email = data_in.user.email,
            phone = data_in.user.phone,
            sex = data_in.user.sex,
            is_active = True,
            password = data_in.user.password,
            role_name = 'clinic_admin'
        )

        signup = users_service.signup(db=db, data_in=admin_signup, flush=True)

        clinic = self.create_with_flush(db=db, data_in=ClinicBase(
            name=data_in.clinic.name,
            detail_address=data_in.clinic.detail_address,
            district=data_in.clinic.district,
            sub_district=data_in.clinic.sub_district,
            contact_phone=data_in.clinic.contact_phone,
            contact_email=data_in.clinic.contact_email,
            clinic_is_active=data_in.clinic.clinic_is_active
        ))

        clinic_user = clinic_user_service.create(db=db, data_in=ClinicUserIn(user_id=handle_result(signup).id, clinic_id=handle_result(clinic).id))
        cli_id = handle_result(clinic).id
        hxclinic_id = "hxclinic"+str(cli_id)

        return ServiceResult({"your_clinic_hxclinicid":hxclinic_id}, status_code=status.HTTP_200_OK)


    def clinic_user_login(self, db: Session, data_in: ClinicLogin):
        hxclinic_id = data_in.hxclinic_id
        clinic_str = hxclinic_id.split("hxclinic")
        clinic_id = int(clinic_str[1])
        
        user_from_identifier = None
        user_email = users_repo.search_by_email(db=db, email_in=data_in.identifier)
        user_phone = users_repo.search_by_phone(db=db, phone_in=data_in.identifier)
        if user_email != None:
            user_from_identifier = user_email
        if user_phone != None:
            user_from_identifier = user_phone


        clinic_check = clinic_user_service.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_from_identifier.id, clinic_id=clinic_id)
        clinic_with_user = handle_result(clinic_check)

        if len(clinic_with_user) == 0:
            return ServiceResult(AppException.ServerError("Invalid Clinic id"))



        return users_service.login(db=db, identifier=data_in.identifier, password=data_in.password)


clinic_service = ClinicService(Clinic, clinic_repo)