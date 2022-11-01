from services import BaseService
from models import PharmacySingleGrn
from schemas import PharmacySingleGrnIn, PharmacySingleGrnUpdate
from repositories import pharmacy_single_grn_repo, ep_medicines_list_repo
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result


class PharmacySingleGrnService(BaseService[PharmacySingleGrn, PharmacySingleGrnIn, PharmacySingleGrnUpdate]):
    
    def all_single_grn(self, db: Session, skip: int, limit: int, grn_id: int):
        all_single_grn = self.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, grn_id = grn_id )
        all_single_grn_data = []
        for i in handle_result(all_single_grn)[1]:
            med_id = i.medicine_id
            medicines = ep_medicines_list_repo.get_one(db=db, id=med_id)
            i.medicine_name = medicines.name
            i.medicine_generic = medicines.generic
            all_single_grn_data.append(i)
        return all_single_grn

pharmacy_single_grn_service = PharmacySingleGrnService(PharmacySingleGrn, pharmacy_single_grn_repo)