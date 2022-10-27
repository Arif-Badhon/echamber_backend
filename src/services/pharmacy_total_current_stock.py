from services import BaseService
from models import PharmacyTotalCurrentStock
from schemas import PharmacyTotalCurrentStockIn, PharmacyTotalCurrentStockUpdate
from repositories import pharmacy_total_current_stock_repo, ep_medicines_list_repo
from exceptions.service_result import handle_result
from sqlalchemy.orm import Session

class PharmacyTotalCurrentStockService(BaseService[PharmacyTotalCurrentStock, PharmacyTotalCurrentStockIn, PharmacyTotalCurrentStockUpdate]):
    def total_current_stock(self, db: Session):
        total_stock = self.get(db=db)
        total_stock_data = []
        for i in handle_result(total_stock):
            med_id = i.medicine_id
            medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
            i.medicine_name = medicines.name
            i.medicine_generic = medicines.generic
            i.medicine_strength = medicines.strength
            total_stock_data.append(i)
        return total_stock

pharmacy_total_current_stock_service = PharmacyTotalCurrentStockService(PharmacyTotalCurrentStock, pharmacy_total_current_stock_repo)