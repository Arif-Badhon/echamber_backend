from sqlalchemy.orm import Session
from exceptions.app_exceptions import AppException
from exceptions.service_result import ServiceResult, handle_result
from services import BaseService, users_service
from models import PatientFamily
from schemas import PatientFamilyIn, PatientFamilyUpdate
from repositories import patient_families_repo
from exceptions import ServiceResult, AppException
from fastapi import status


class PatientFamilyService(BaseService[PatientFamily, PatientFamilyIn, PatientFamilyUpdate]):
    
    def search_by_user_id(self, db: Session, user_id:int):
        data = self.repo.search_by_user_id(db=db, user_id=user_id)


        data_with_name = []
        # here name merge by their user id
        for i in data:
            i.relation_from_name = handle_result(users_service.get_one(db=db,id=i.user_id)).name
            i.relation_with_name = handle_result(users_service.get_one(db=db,id=i.relation_with)).name
            data_with_name.append(i)

        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_200_OK)
    
    def member_status(self, db: Session, user_id: int, relationship_status: str):
        data = self.repo.member_status(db=db, user_id=user_id, relationship_status=relationship_status)

        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        return ServiceResult(data, status_code=status.HTTP_200_OK)
    
    def update_relationship_status(self, db: Session, user_id: int, id:int, relationship_status: str):
        get = self.get_one(db=db, id=id)
        handle_get = handle_result(get)
        
        if user_id != handle_get.user_id:
            return ServiceResult(AppException.NotAccepted('user id not matched'))

        if not relationship_status in ['accepted', 'pending', 'reject']:
            return ServiceResult(AppException.NotAccepted('relationship status not matched'))

        update = self.repo.update(db=db, id=id, data_update=PatientFamilyUpdate(relationship_status=relationship_status))
        
        if not update:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(update, status_code=status.HTTP_200_OK)


patient_families_service = PatientFamilyService(PatientFamily, patient_families_repo)