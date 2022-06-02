from services import BaseService
from models import ImagesLog
from schemas import ImageLogIn, ImageLogUpdate
from repositories import image_log_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class ImageLogService(BaseService[ImagesLog, ImageLogIn, ImageLogUpdate]):
    
    def last_profile_pic(self, db: Session, user_id: int):
        last_pp = self.repo.last_profile_pic(db=db, user_id=user_id)

        if not last_pp:
            return ServiceResult(AppException.NotFound("Image not found"))
        else:
            return ServiceResult(last_pp, status_code=status.HTTP_200_OK)



    def patient_all_reports(self, db: Session, user_id: int, skip: int, limit:int):

        all_reports = self.repo.patient_all_reports(db=db, user_id=user_id, skip=skip, limit=limit)

        if not all_reports:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_reports, status_code=status.HTTP_200_OK)



image_log_service = ImageLogService(ImagesLog, image_log_repo)