from repositories import BaseRepo
from models import ImagesLog
from schemas import ImageLogIn, ImageLogUpdate
from sqlalchemy.orm import Session
from sqlalchemy import desc

class ImageLogRepo(BaseRepo[ImagesLog, ImageLogIn, ImageLogUpdate]):
    def last_profile_pic(self, db:Session, user_id: int):
        query = db.query(self.model).filter(self.model.user_id == user_id).filter(self.model.service_name=='propic').order_by(desc(self.model.created_at)).first()
        return query

    def patient_all_reports(self, db: Session, user_id: int, skip: int, limit:int):
        query = db.query(self.model).filter(self.model.user_id == user_id).filter(self.model.service_name == 'patient_report').order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return query
        
image_log_repo = ImageLogRepo(ImagesLog)