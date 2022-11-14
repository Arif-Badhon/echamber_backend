from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from services import BaseService,pharmacy_purchase_order_service
from models import PharmacyPurchaseSingleOrder
from schemas import PharmacyPurchaseSingleOrderIn, PharmacyPurchaseSingleOrderUpdate
from repositories import pharmacy_purchase_single_order_repo, ep_medicines_list_repo

class PharmacyPurchaseSingleOrderService(BaseService[PharmacyPurchaseSingleOrder, PharmacyPurchaseSingleOrderIn, PharmacyPurchaseSingleOrderUpdate]):
    
    def all_single_order(self, db: Session, skip: int, limit: int, purchase_order_id: int):
        all_purchase_single_order = self.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, purchase_order_id =purchase_order_id )
        all_single_order_data = []
        for i in handle_result(all_purchase_single_order)[1]:
            med_id = i.medicine_id
            medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
            i.medicine_name = medicines.name
            i.medicine_generic = medicines.generic
            i.pharmaceuticals = medicines.pharmaceuticals
            all_single_order_data.append(i)
        return all_purchase_single_order

    def all_single_order_by_purchase_num(self, db: Session, skip: int, limit: int, purchase_number: str):
        purchase_order_by_purchase_num = pharmacy_purchase_order_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, purchase_number=purchase_number)
        purchase_order_id = handle_result(purchase_order_by_purchase_num)[1][0].id
        all_purchase_single_order = self.all_single_order(db=db, skip=skip, limit=limit, purchase_order_id=purchase_order_id)
        return all_purchase_single_order

    def purchase_oder_by_purchase_num(self, db: Session, skip: int, limit: int, purchase_number: str):
        purchase_order_by_purchase_num = pharmacy_purchase_order_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, purchase_number=purchase_number)
        return purchase_order_by_purchase_num


pharmacy_purchase_single_order_service = PharmacyPurchaseSingleOrderService(PharmacyPurchaseSingleOrder, pharmacy_purchase_single_order_repo)
