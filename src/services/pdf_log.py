from repositories import pdf_log_repo
from services import BaseService
from models import PdfLog
from schemas import PdfLogIn, PdfLogUpdate
from sqlalchemy.orm import Session
from exceptions import AppException, ServiceResult
from fastapi import status


class PdfLogService(BaseService[PdfLog, PdfLogIn, PdfLogUpdate]):
    
    def patient_all_reports(self, db: Session, user_id: int, skip: int, limit:int):

        all_reports = self.repo.patient_all_reports(db=db, user_id=user_id, skip=skip, limit=limit)

        if not all_reports:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_reports, status_code=status.HTTP_200_OK)



pdf_log_service = PdfLogService(PdfLog, pdf_log_repo)