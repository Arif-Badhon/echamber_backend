from repositories import BaseRepo
from schemas import ServiceOrderIn, ServiceOrderUpdate
from models import ServiceOrder
from sqlalchemy.orm import Session
from sqlalchemy import desc

class ServiceOrderService(BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):
    
    def all_service_order_search(self, db: Session, skip: int=0, limit:int=15):
        data = db.query(self.model).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        results = db.query(self.model).all()
        
        return [{"results": len(results)}, data]


service_order_repo = ServiceOrderService(ServiceOrder)