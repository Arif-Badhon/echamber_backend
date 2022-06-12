from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate
from repositories import BaseRepo


service_order_repo = BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate](ServiceOrder)