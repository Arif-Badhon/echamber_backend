from models import MedicineOrder
from schemas import MedicineOrderInWithService, MedicineOrderUpdate
from repositories import BaseRepo

medicine_order_repo = BaseRepo[MedicineOrder, MedicineOrderInWithService, MedicineOrderUpdate](MedicineOrder)