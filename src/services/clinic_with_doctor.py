from services import BaseService, clinic_user_service, roles_service
from models import ClinicWithDoctor
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate, ClinicActivityIn
from repositories import clinic_with_doctor_repo, clinic_activity_repo, users_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException
from fastapi import status



class ClinicWithDoctorService(BaseService[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate]):
    
    def check_user_with_clinic(self, db: Session, user_id:int, clinic_id:int):
        check = clinic_user_service.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, user_id=user_id, clinic_id=clinic_id)
        check_user_clinic_id = handle_result(check)

        if len(check_user_clinic_id) == 1:
            return True
        else:
            return False

    def check_doctor_with_clinic(self, db: Session, doctor_id:int, clinic_id:int):
        check = self.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=False, doctor_id=doctor_id, clinic_id=clinic_id)
        check_doc_clinic_id = handle_result(check)

        if len(check_doc_clinic_id) == 1:
            return True
        else:
            return False
    
    def doctor_append(self, db: Session, doctor_user_id: int, clinic_id:int,  user_id: int):
        
        clinic_with_user = self.check_user_with_clinic(db=db, user_id=user_id, clinic_id=clinic_id)
        if clinic_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Clinic ID")) 

        doctor_with_clinic = self.check_doctor_with_clinic(db=db, doctor_id=doctor_user_id, clinic_id=clinic_id)
        if doctor_with_clinic == True:
            return ServiceResult(AppException.ServerError("Already registered in this clinic"))

        get_doctor = users_repo.get_one(db=db, id=doctor_user_id)
        if not get_doctor:
            return ServiceResult(AppException.ServerError("Doctor not exist."))
        else:
            doc_role = roles_service.role_id_by_name(db=db, name='doctor')
            print(get_doctor.role_id)
            if get_doctor.role_id != doc_role:
                return ServiceResult(AppException.ServerError("Not valid doctor"))




        doc_append = clinic_with_doctor_repo.create_with_flush(db=db, data_in=ClinicWithDoctorIn(clinic_id=  clinic_id,doctor_id= doctor_user_id))
        
        doctor_append_data = ClinicActivityIn(
            clinic_id = clinic_id,
            user_id=user_id,
            service_name="doctor_append",
            service_received_id=doctor_user_id,
            remark=""
        )

        doctor_append = clinic_activity_repo.create(db=db, data_in=doctor_append_data)

        if not doctor_append:
            return ServiceResult(AppException.ServerError("Problem with doctor append"))
        else:
            return ServiceResult(doctor_append, status_code=status.HTTP_201_CREATED)


    def search_by_clinic_id(self, db: Session, skip: int, limit: int, clinic_id: str):
        clinic_doctor = self.repo.search_by_clinic_id(db= db, skip=skip, limit=limit, clinic_id=clinic_id)
        return clinic_doctor


clinic_with_doctor_service = ClinicWithDoctorService(ClinicWithDoctor, clinic_with_doctor_repo)
