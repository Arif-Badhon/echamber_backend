from services import BaseService
from repositories import service_order_repo
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate

service_order_service = BaseService[ServiceOrder,ServiceOrderIn, ServiceOrderUpdate](ServiceOrder, service_order_repo)