from exceptions import service_result
from services import BaseService
from models import PharmacyPurchaseOrder
from schemas import PharmacyPurchaseOrderIn, PharmacyPurchaseOrderUpdate, PharmacyPurchaseOrderBase, PharmacyPurchaseOrderWithSingleOrder, PharmacyPurchaseSingleOrderWithPurchaseOrder
from repositories import pharmacy_purchase_order_repo, pharmacy_purchase_single_order_repo
from sqlalchemy.orm import Session
from exceptions.service_result import ServiceResult
from exceptions.app_exceptions import AppException


class PharmacyPurchaseOrderService(BaseService[PharmacyPurchaseOrder, PharmacyPurchaseOrderBase, PharmacyPurchaseOrderUpdate]):

    def submit(self, data_in: PharmacyPurchaseOrderWithSingleOrder, db: Session):
        
        pur_num = self.repo.get_by_key(db=db, skip=0, limit=100, descending=False, count_results=True, purchase_number=data_in.purchase_order.purchase_number)

        if pur_num[0]["results"] !=0:
            return ServiceResult(AppException.ServerError("Purchase Number Already Registered"))


        purchase_order = pharmacy_purchase_order_repo.create_with_flush(db = db, data_in = PharmacyPurchaseOrderBase(
            total_amount_dp=data_in.purchase_order.total_amount_dp,
            discount=data_in.purchase_order.discount,
            payable_amount=data_in.purchase_order.payable_amount,
            paid_amount=data_in.purchase_order.paid_amount,
            due_amount=data_in.purchase_order.due_amount,
            subtotal_amount=data_in.purchase_order.subtotal_amount,
            pharmaceuticals_name_id=data_in.purchase_order.pharmaceuticals_name_id,
            purchase_number=data_in.purchase_order.purchase_number,
            user_id=data_in.purchase_order.user_id,
            pharmacy_id=data_in.purchase_order.pharmacy_id,
            remarks=data_in.purchase_order.remarks,
            expected_delivery_date=data_in.purchase_order.expected_delivery_date,
            delivery_status=data_in.purchase_order.delivery_status
        ))

        if data_in.single_purchase_order and len(data_in.single_purchase_order) != 0:
            for i in data_in.single_purchase_order:
                single_order = pharmacy_purchase_single_order_repo.create_with_flush(db=db, data_in=PharmacyPurchaseSingleOrderWithPurchaseOrder(quantity=i.quantity, unit_price_dp=i.unit_price_dp, total_price_dp=i.total_price_dp, discount=i.discount, payable_prize_dp=i.payable_prize_dp, medicine_id=i.medicine_id, purchase_order_id=purchase_order.id))

        db.commit()

        return ServiceResult({"msg": "Success"}, status_code=200)


    def get_purchase_order_with_grn(self, db: Session, skip: int, limit: int):
        purchase_order = self.repo.get_purchase_order_with_grn(db= db, skip=skip, limit=limit)
        return purchase_order

    def get_purchase_order_without_grn(self, db: Session, skip: int, limit: int):
        purchase_order = self.repo.get_purchase_order_without_grn(db= db, skip=skip, limit=limit)
        return purchase_order

pharmacy_purchase_order_service = PharmacyPurchaseOrderService(PharmacyPurchaseOrder, pharmacy_purchase_order_repo)