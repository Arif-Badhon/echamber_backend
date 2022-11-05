from exceptions.service_result import handle_result
from services import BaseService
from models import PharmacyEverySingleStock
from schemas import PharmacyEverySingleStockIn, PharmacyEverySingleStockUpdate
from repositories import pharmacy_every_single_stock_repo, ep_medicines_list_repo
from sqlalchemy.orm import Session


class PharmacyEverySingleStockService(BaseService[PharmacyEverySingleStock, PharmacyEverySingleStockIn, PharmacyEverySingleStockUpdate]):
    
    def all_single_stock(self, db:Session):
        all_stock = self.get(db=db)
        all_stock_data = []
        for i in handle_result(all_stock):
            med_id = i.medicine_id
            medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
            i.medicine_name = medicines.name
            i.medicine_generic = medicines.generic
            i.medicine_strength = medicines.strength
            i.pharmaceuticals = medicines.pharmaceuticals
            all_stock_data.append(i)
        return all_stock 


pharmacy_every_single_stock_servive = PharmacyEverySingleStockService(PharmacyEverySingleStock, pharmacy_every_single_stock_repo)