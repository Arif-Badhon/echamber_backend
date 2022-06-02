from sqlalchemy import desc
from repositories import BaseRepo
from schemas import PdfLogIn, PdfLogUpdate
from models import PdfLog
from sqlalchemy.orm import Session

class PdfLogRepo(BaseRepo[PdfLog, PdfLogIn, PdfLogUpdate]):
    
    def patient_all_reports(self, db: Session, user_id: int, skip: int, limit:int):
        query = db.query(self.model).filter(self.model.user_id == user_id).filter(self.model.service_name == 'patient_report').order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return query


pdf_log_repo = PdfLogRepo(PdfLog)