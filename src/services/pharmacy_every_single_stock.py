from exceptions.service_result import handle_result
from services import BaseService
from models import PharmacyEverySingleStock
from schemas import PharmacyEverySingleStockIn, PharmacyEverySingleStockUpdate
from repositories import pharmacy_every_single_stock_repo, ep_medicines_list_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


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


    def get_expired_medicine(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        expired_medicine = self.repo.get_expired_medicine(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
        if not expired_medicine:
            return ServiceResult(AppException.NotFound("no medicine found"))
        else:
            for i in expired_medicine[1]:
                all_stock_data = []
                med_id = i.medicine_id
                medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
                i.medicine_name = medicines.name
                i.medicine_generic = medicines.generic
                i.medicine_strength = medicines.strength
                i.pharmaceuticals = medicines.pharmaceuticals
                all_stock_data.append(i)
                return ServiceResult(expired_medicine, status_code=status.HTTP_200_OK)

    def get_nearly_expired_medicine(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        nearly_expired_medicine = self.repo.get_nearly_expired_medicine(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)

        if not nearly_expired_medicine:
            return ServiceResult(AppException.NotFound("no medicine found"))
        else:
            for i in nearly_expired_medicine[1]:
                all_stock_data = []
                med_id = i.medicine_id
                medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
                i.medicine_name = medicines.name
                i.medicine_generic = medicines.generic
                i.medicine_strength = medicines.strength
                i.pharmaceuticals = medicines.pharmaceuticals
                all_stock_data.append(i)
            return ServiceResult(nearly_expired_medicine, status_code=status.HTTP_200_OK)



pharmacy_every_single_stock_servive = PharmacyEverySingleStockService(PharmacyEverySingleStock, pharmacy_every_single_stock_repo)