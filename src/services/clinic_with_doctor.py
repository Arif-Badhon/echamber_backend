from services import BaseService, clinic_user_service, doctors_service
from models import ClinicWithDoctor
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate, ClinicWithDoctorAdd, ClinicUserIn, clinic_user
from repositories import clinic_with_doctor_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException



class ClinicWithDoctorService(BaseService[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate]):
    
    def check_user_with_clinic(self, db: Session, user_id:int, clinic_id:int):
        check = clinic_user_service.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id, clinic_id=clinic_id)
        check_user_ph_id = handle_result(check)

        if len(check_user_ph_id) == 1:
            return True
        else:
            return False
    
    def doctor_append(self, db: Session, doctor_user_id: int, clinic_id:int,  user_id: int):
        
        clinic_with_user = self.check_user_with_clinic(db=db, user_id=user_id, clinic_id=clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID")) 

        doc_append = clinic_with_doctor_repo.create_with_flush(db=db, data_in=ClinicWithDoctorIn(clinic_id=  clinic_id,doctor_id= doctor_user_id))
        
        db.commit()
        return ServiceResult({"msg": "Success"}, status_code=200)

clinic_with_doctor_service = ClinicWithDoctorService(ClinicWithDoctor, clinic_with_doctor_repo)
