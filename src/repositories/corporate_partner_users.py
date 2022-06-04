from sqlalchemy import desc
from models import CorporatePartnerUsers
from schemas import CorporatePartnerUserIn, CorporatePartnerUserUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session

class CorporatePartnerUserRepo(BaseRepo[CorporatePartnerUsers, CorporatePartnerUserIn, CorporatePartnerUserUpdate]):
    
    def search_user_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.users_id == id).first()

    # BackLog sqlalchemy join needed
    def all_clients(self, db: Session, skip: int, limit: int):
        clients =  db.query(self.model).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return clients


corporate_partner_user_repo = CorporatePartnerUserRepo(CorporatePartnerUsers)