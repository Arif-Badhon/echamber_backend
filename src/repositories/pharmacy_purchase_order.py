from repositories import BaseRepo
from models import PharmacyPurchaseOrder, PharmacyGrn
from schemas import PharmacyPurchaseOrderIn, PharmacyPurchaseOrderUpdate
from sqlalchemy.orm import Session


class PharmacyPurchaseOrderRepo(BaseRepo[PharmacyPurchaseOrder, PharmacyPurchaseOrderIn, PharmacyPurchaseOrderUpdate]):

    def get_purchase_order_by_pharmacy_id(self, db: Session, pharmacy_id: int, skip: int, limit: int):
        data_count = db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).all()
        data = db.query(self.model).filter(self.model.pharmacy_id == pharmacy_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    def get_purchase_order_with_grn(self, db: Session, skip: int, limit: int):
        data_count = db.query(self.model, PharmacyGrn).join(self.model, self.model.id == PharmacyGrn.purchase_order_id).filter(self.model.id == PharmacyGrn.purchase_order_id).all()
        data = db.query(self.model, PharmacyGrn).join(self.model, self.model.id == PharmacyGrn.purchase_order_id).filter(self.model.id == PharmacyGrn.purchase_order_id).offset(skip).limit(limit).all()
        return [{"results": len(data_count)}, data]

    # def get_purchase_order_without_grn(self, db: Session, skip: int, limit: int):
    #     all_purchase = db.query(self.model).all()
    #     purchase_with_grn = db.query(self.model).filter(self.model.id == PharmacyGrn.purchase_order_id).offset(skip).limit(limit).all()
    #     return [all_purchase, purchase_with_grn]

    def get_purchase_order_without_grn(self, db: Session):
        data = db.query(self.model).filter(self.model.id.not_in(db.query(PharmacyGrn.purchase_order_id).all())).all()
        return data


pharmacy_purchase_order_repo = PharmacyPurchaseOrderRepo(PharmacyPurchaseOrder)
