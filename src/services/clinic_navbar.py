from services import BaseService, clinic_with_doctor_service
from models import ClinicNavbar
from schemas import ClinicNavbarIn, ClinicNavbarUpdate
from repositories import clinic_navbar_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions import ServiceResult, AppException


class ClinicNavbarService(BaseService[ClinicNavbar, ClinicNavbarIn, ClinicNavbarUpdate]):
    
    def clinic_nav(self, db: Session, data_in: ClinicNavbarIn, user_id: int):

        clinic_nav = self.create_with_flush(db=db, data_in=ClinicNavbarIn(
            clinic_id=data_in.clinic_id,
            nav_text=data_in.nav_text,
            nav_href=data_in.nav_href
        ))

        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=handle_result(clinic_nav).clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))

        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)


    def get_nav_by_clinic_id(self, db: Session, clinic_id: int):
        get_nav = self.repo.get_nav_by_clinic_id(db=db, clinic_id=clinic_id)
        return get_nav

clinic_navbar_service = ClinicNavbarService(ClinicNavbar, clinic_navbar_repo)
