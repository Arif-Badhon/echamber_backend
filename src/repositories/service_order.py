from models import ServiceOrder, User
from schemas import ServiceOrderIn, ServiceOrderUpdate
from repositories import BaseRepo


class ServiceOrderRepo(BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):

    def service_with_patient(self, service_id: int, customer_name: str, customer_phone: str, address: str, service_name: str, order_date: str, order_status: str, skip: int, limit: int):
        return


service_order_repo = ServiceOrderRepo(ServiceOrder)
