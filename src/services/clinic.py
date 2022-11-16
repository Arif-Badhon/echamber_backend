from services import BaseService, users_service, doctor_qualifications_service, doctor_specialities_service, doctors_service, user_details_service, CreateSchemaType
from .clinic_with_doctor import clinic_with_doctor_service
from models import Clinic
from schemas import ClinicIn, ClinicUpdate, ClinicUserWithClinic, UserCreate, ClinicBase, ClinicUserIn, ClinicLogin
from schemas import DoctorSignup, DoctorIn,  DoctorQualilficationIn, DoctorSpecialityIn, UserDetailIn, ClinicActivityIn
from repositories import clinic_repo, users_repo, clinic_activity_repo
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
            clinic_license=data_in.clinic.clinic_license,
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


    def clinic_doctor_signup(self, db: Session, data_in: DoctorSignup, clinic_id: int, user_id: int):

        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))

        signup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=False,
            password=data_in.password,
            role_name='doctor'
        )

        signup_user = users_service.signup(db, data_in=signup_data, flush=True)

        doctor_data = DoctorIn(
            user_id=handle_result(signup_user).id,
            bmdc=data_in.bmdc
        )

        doctor_user = doctors_service.create_with_flush(db, data_in=doctor_data)

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

        specialities_user = doctor_specialities_service.create_with_flush(
            db, data_in=specialities_data)


        doctor_user_id = handle_result(signup_user).id
        append = clinic_with_doctor_service.doctor_append(db=db, doctor_user_id=doctor_user_id, clinic_id=clinic_id, user_id=user_id)

        return ServiceResult({"msg": "Success"}, status_code=200)

    def clinic_patient_signup(self, db: Session, data_in: CreateSchemaType, clinic_id: int, user_id: int):

        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))      

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

        ud = user_details_service.create_with_flush(db, data_in=user_details_data)

        if not ud:
            return ServiceResult(AppException.ServerError(
                "Problem with patient registration."))
        else:
            clinic_patient_data = ClinicActivityIn(
            clinic_id = clinic_id,
            user_id=user_id,
            service_name="patient_registration",
            service_received_id=handle_result(signup_user).id,
            remark=""
        )

        register_patient = clinic_activity_repo.create(db=db, data_in=clinic_patient_data)

        if not register_patient:
            return ServiceResult(AppException.ServerError("Problem with patient registration"))
        else:
            return ServiceResult(register_patient, status_code=status.HTTP_201_CREATED)


clinic_service = ClinicService(Clinic, clinic_repo)