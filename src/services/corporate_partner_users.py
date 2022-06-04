from models import CorporatePartnerUsers
from schemas import CorporatePartnerUserIn, CorporatePartnerUserUpdate
from repositories import corporate_partner_user_repo
from services import BaseService
from sqlalchemy.orm import Session
from exceptions import ServiceResult
from fastapi import status

class CorporatePartnerUserService(BaseService[CorporatePartnerUsers, CorporatePartnerUserIn, CorporatePartnerUserUpdate]):
    
    def all_clients(self, db: Session, skip: int, limit: int):

        clients = self.repo.all_clients(db=db, skip=skip, limit=limit)
        
        if not clients:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(clients, status_code=status.HTTP_201_CREATED) 


corporate_partner_user_service = CorporatePartnerUserService(CorporatePartnerUsers, corporate_partner_user_repo)