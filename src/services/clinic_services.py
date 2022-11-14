from services import BaseService, clinic_with_doctor_service
from models import ClinicServices
from schemas import ClinicServicesIn, ClinicServicesUpdate, ClinicServicesBase
from repositories import clinic_services_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions import ServiceResult, AppException

class ClinicServicesService(BaseService[ClinicServices, ClinicServicesIn, ClinicServicesUpdate]):

    def add_clinic_services(self, db: Session, data_in: ClinicServicesBase, user_id: int):

        clinic_services = self.create_with_flush(db=db, data_in=ClinicServicesIn(
            clinic_id=data_in.clinic_id,
            servive_name=data_in.servive_name,
            service_details=data_in.service_details,
            service_price=data_in.service_price,
            image_id=data_in.image_id
        ))


        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=handle_result(clinic_services).clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))

        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)

        
    def get_clinic_services_by_clinic_id(self, db: Session, clinic_id: int):

        clinic_services = self.repo.get_clinic_services_by_clinic_id(db=db, clinic_id=clinic_id)
        return clinic_services


clinic_services_service = ClinicServicesService(ClinicServices, clinic_services_repo)