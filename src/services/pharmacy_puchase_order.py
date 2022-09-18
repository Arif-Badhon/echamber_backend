from exceptions import service_result
from services import BaseService
from models import PharmacyPurchaseOrder
from schemas import PharmacyPurchaseOrderIn, PharmacyPurchaseOrderUpdate, PharmacyPurchaseOrderBase, PharmacyPurchaseOrderWithSingleOrder, PharmacyPurchaseSingleOrderWithPurchaseOrder
from repositories import pharmacy_purchase_order_repo, pharmacy_purchase_single_order_repo
from sqlalchemy.orm import Session
from exceptions.service_result import ServiceResult


class PharmacyPurchaseOrderService(BaseService[PharmacyPurchaseOrder, PharmacyPurchaseOrderBase, PharmacyPurchaseOrderUpdate]):

    def submit(self, data_in: PharmacyPurchaseOrderWithSingleOrder, db: Session):

        purchase_order = pharmacy_purchase_order_repo.create_with_flush(db = db, data_in = PharmacyPurchaseOrderBase(
            total_amount_dp=data_in.purchase_order.total_amount_dp,
            discount=data_in.purchase_order.discount,
            payable_amount=data_in.purchase_order.payable_amount,
            paid_amount=data_in.purchase_order.payable_amount,
            due_amount=data_in.purchase_order.due_amount,
            subtotal_amount=data_in.purchase_order.subtotal_amount,
            pharmaceuticals_name_id=data_in.purchase_order.pharmaceuticals_name_id,
            purchase_number=data_in.purchase_order.purchase_number,
            user_id=data_in.purchase_order.user_id,
            pharmacy_id=data_in.purchase_order.pharmacy_id,
            remarks=data_in.purchase_order.remarks
        ))

        if data_in.single_purchase_order and len(data_in.single_purchase_order) != 0:
            for i in data_in.single_purchase_order:
                single_order = pharmacy_purchase_single_order_repo.create_with_flush(db=db, data_in=PharmacyPurchaseSingleOrderWithPurchaseOrder(quantity=i.quantity, unit_price_dp=i.unit_price_dp, discount=i.discount, payable_prize_dp=i.payable_prize_dp, medicine_id=i.medicine_id, purchase_order_id=purchase_order.id))

        db.commit()

        return ServiceResult("Success")

pharmacy_purchase_order_service = PharmacyPurchaseOrderService(PharmacyPurchaseOrder, pharmacy_purchase_order_repo)