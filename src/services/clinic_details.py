from services import BaseService, clinic_with_doctor_service
from models import ClinicDetails
from schemas import ClinicDetailsIn, ClinicDetailsUpdate
from repositories import clinic_details_repo
from sqlalchemy.orm import Session
from exceptions import AppException,ServiceResult
from exceptions.service_result import handle_result


class ClinicDetailsService(BaseService[ClinicDetails, ClinicDetailsIn, ClinicDetailsUpdate]):
    
    def clinic_details_add(self, db: Session, data_in: ClinicDetailsIn, user_id: int):
        
        clinic_details = self.create_with_flush(db=db, data_in=ClinicDetailsIn(
            clinic_id=data_in.clinic_id,
            title=data_in.title,
            sub_title=data_in.sub_title,
            title_bg_image_id=data_in.title_bg_image_id,
            about=data_in.about,
            about_image_id=data_in.about_image_id,
            contuct_us=data_in.contuct_us,
            footer=data_in.footer
        ))

        clinic_with_user = clinic_with_doctor_service.check_user_with_clinic(db=db, user_id=user_id, clinic_id=handle_result(clinic_details).clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID"))

        detail = self.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=True, clinic_id=handle_result(clinic_details).clinic_id)
        result = handle_result(detail)
        print(result[0]["results"])
        if result[0]["results"] > 1:
            return ServiceResult(AppException.ServerError("Already added please update"))

        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)
    
    def get_details_by_clinic_id(self, db: Session, clinic_id: int):
        get_details = self.repo.get_details_by_clinic_id(db=db, clinic_id=clinic_id)
        return get_details


clinic_details_service = ClinicDetailsService(ClinicDetails, clinic_details_repo) 