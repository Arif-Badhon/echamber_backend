from sqlalchemy.orm import Session
from services import BaseService
from repositories import service_order_repo, admin_panel_activity_repo
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate


class ServiceOrderService(BaseService[ServiceOrder,ServiceOrderIn, ServiceOrderUpdate]):
    
    def created_by_employee(self, db: Session,):
        return

service_order_service = ServiceOrderService(ServiceOrder, service_order_repo)