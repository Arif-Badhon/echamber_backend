from services import BaseService, users_service
from models import Clinic
from schemas import ClinicIn, ClinicUpdate, ClinicUserWithClinic, UserCreate, ClinicBase, ClinicUserIn, ClinicLogin
from repositories import clinic_repo, users_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from .clinic_user import clinic_user_service

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
        return clinic_user


clinic_service = ClinicService(Clinic, clinic_repo)