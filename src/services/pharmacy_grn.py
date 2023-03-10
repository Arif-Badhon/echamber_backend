from services import BaseService, pharmacy_service
from models import PharmacyGrn
from schemas import PharmacyGrnIn, PharmacyGrnUpdate, PharmacyGrnWithSingleGrn, PharmacySingleGrnWithGrn, PharmacySingleGrnForStock, PharmacyTotalCurrentStockIn, PharmacyTotalCurrentStockUpdate
from repositories import pharmacy_grn_repo, pharmacy_single_grn_repo, pharmacy_every_single_stock_repo, pharmacy_total_current_stock_repo
from sqlalchemy.orm import Session
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException

class PharmacyGrnService(BaseService[PharmacyGrn, PharmacyGrnIn, PharmacyGrnUpdate]):
    
    def submit(self, data_in: PharmacyGrnWithSingleGrn, db: Session, user_id: int):
        grn = pharmacy_grn_repo.create_with_flush(db = db, data_in=PharmacyGrnIn(
            total_amount_dp=data_in.grn.total_amount_dp,
            grn_number=data_in.grn.grn_number,
            total_amount_mrp=data_in.grn.total_amount_mrp,
            total_vat_mrp=data_in.grn.total_vat_mrp,
            total_discount_mrp=data_in.grn.total_discount_mrp,
            discount_amount=data_in.grn.discount_amount,
            total_cost_mrp=data_in.grn.total_cost_mrp,
            pharmaceuticals_name_id=data_in.grn.pharmaceuticals_name_id,
            purchase_order_id=data_in.grn.purchase_order_id,
            pharmacy_id=data_in.grn.pharmacy_id,
            paid_amount=data_in.grn.paid_amount,
            due_amount=data_in.grn.due_amount
        ))

        if data_in.single_grn and len(data_in.single_grn) != 0:
            for i in data_in.single_grn:
                single_grn = pharmacy_single_grn_repo.create_with_flush(db=db, data_in=PharmacySingleGrnWithGrn(
                    dp_prize=i.dp_prize,
                    quantity=i.quantity,
                    mrp=i.mrp,
                    vat=i.vat,
                    discount=i.discount,
                    discount_amount= i.discount_amount,
                    cost=i.cost,
                    expiry_date=i.expiry_date,
                    batch_number=i.batch_number,
                    medicine_id=i.medicine_id,
                    pack_size=i.pack_size,
                    grn_id=grn.id
                ))

                single_stock = pharmacy_every_single_stock_repo.create_with_flush(db=db, data_in=PharmacySingleGrnForStock(
                    quantity=i.quantity,
                    expiry_date=i.expiry_date,
                    batch_number=i.batch_number,
                    medicine_id=i.medicine_id,
                    pack_size=i.pack_size,
                    single_grn_id=single_grn.id,
                    pharmacy_id=data_in.grn.pharmacy_id
                ))

                check_medicine_pharmacy_id = pharmacy_total_current_stock_repo.get_by_two_key(db=db, skip=0, limit=100, descending=False, count_results=True, medicine_id =i.medicine_id, pharmacy_id=single_stock.pharmacy_id)
                if check_medicine_pharmacy_id[0]["results"] != 0:
                    update_total_stock = pharmacy_total_current_stock_repo.update(db=db, id=check_medicine_pharmacy_id[1][0].id, data_update=PharmacyTotalCurrentStockUpdate(
                        quantity=check_medicine_pharmacy_id[1][0].quantity + single_stock.quantity
                    ))

                else:
                    total_stock = pharmacy_total_current_stock_repo.create_with_flush(db=db, data_in=PharmacyTotalCurrentStockIn(
                        quantity=single_stock.quantity,
                        medicine_id=single_stock.medicine_id,
                        pharmacy_id=single_stock.pharmacy_id
                    ))

        pharmacy_with_user = pharmacy_service.check_user_with_pharmacy(db=db, user_id=user_id, pharmacy_id=grn.pharmacy_id)
        if pharmacy_with_user == False:
            return ServiceResult(AppException.ServerError("Invalid Pharmacy ID"))

        db.commit()

        return ServiceResult({"msg": "Success"}, status_code=200)


    def get_grn_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        get_grn = self.repo.get_grn_by_pharmacy_id(db=db, pharmacy_id=pharmacy_id, skip=skip, limit=limit)
        return get_grn

pharmacy_grn_service = PharmacyGrnService(PharmacyGrn, pharmacy_grn_repo)