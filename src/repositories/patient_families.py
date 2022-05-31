from sqlalchemy import desc
from repositories import BaseRepo, ModelType
from schemas import PatientFamilyIn, PatientFamilyUpdate
from models import PatientFamily
from sqlalchemy.orm import Session


class PatintFamilyRepo(BaseRepo[PatientFamily, PatientFamilyIn, PatientFamilyUpdate]):
    
    def search_by_user_id(self, db: Session, user_id: int) -> ModelType:
        query = db.query(self.model).order_by(desc(self.model.created_at)).filter(self.model.user_id == user_id).all()
        return query

    def member_status(self, db: Session, user_id: int, relationship_status:str):
        query = db.query(self.model).order_by(desc(self.model.created_at)).filter(self.model.user_id == user_id).filter(self.model.relationship_status == relationship_status).all()
        return query

        
patient_families_repo = PatintFamilyRepo(PatientFamily)