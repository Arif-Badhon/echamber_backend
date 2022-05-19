from repositories import BaseRepo
from schemas import ServiceOrderIn, ServiceOrderUpdate
from models import ServiceOrder

service_order_repo = BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate](ServiceOrder)