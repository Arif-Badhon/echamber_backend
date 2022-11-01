from models import ServiceOrder, User
from schemas import ServiceOrderIn, ServiceOrderUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session


class ServiceOrderRepo(BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):

    def service_with_patient(self, db: Session,  service_id: int, customer_name: str, customer_phone: str, address: str, service_name: str, order_date: str, order_status: str, skip: int, limit: int):
        data = db.query(ServiceOrder, User).join(User, User.id == ServiceOrder.patient_id).all()
        return data


service_order_repo = ServiceOrderRepo(ServiceOrder)
