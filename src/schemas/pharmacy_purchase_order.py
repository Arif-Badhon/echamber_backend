from datetime import datetime
from pydantic import BaseModel
from typing import List, Optional


class PharmacyPurchaseOrderBase(BaseModel):
    total_amount_dp: Optional[float] = None
    discount: Optional[float] = None
    payable_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    due_amount: Optional[float] = None
    subtotal_amount: Optional[float] = None
    pharmaceuticals_name_id: Optional[int] = None
    purchase_number: Optional[str] = None
    user_id: Optional[int] = None
    pharmacy_id: Optional[int] = None
    remarks: Optional[str] = None


class PharmacyPurchaseOrderIn(PharmacyPurchaseOrderBase):
    pass


class PharmacyPurchaseOrderUpdate(BaseModel):
    total_amount_dp: Optional[float] = None
    discount: Optional[float] = None
    payable_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    due_amount: Optional[float] = None
    subtotal_amount: Optional[float] = None
    pharmaceuticals_name_id: Optional[int] = None
    purchase_number: Optional[str] = None
    user_id: Optional[int] = None
    pharmacy_id: Optional[int] = None
    remarks: Optional[str] = None


class PharmacyPurchaseOrderOut(PharmacyPurchaseOrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Single purchase order


class PharmacyPurchaseSingleOrderBase(BaseModel):
    quantity: Optional[int] = None
    unit_price_dp: Optional[float] = None
    total_price_dp: Optional[float] = None
    discount: Optional[float] = None
    payable_prize_dp: Optional[float] = None
    medicine_id: Optional[int] = None


class PharmacyPurchaseSingleOrderIn(PharmacyPurchaseSingleOrderBase):
    pass

class PharmacyPurchaseSingleOrderWithPurchaseOrder(PharmacyPurchaseSingleOrderBase):
    purchase_order_id: int


class PharmacyPurchaseSingleOrderUpdate(BaseModel):
    quantity: Optional[int] = None
    unit_price_dp: Optional[float] = None
    total_price_dp: Optional[float] = None
    discount: Optional[float] = None
    payable_prize_dp: Optional[float] = None
    medicine_id: Optional[int] = None


class PharmacyPurchaseSingleOrderOut(PharmacyPurchaseSingleOrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PharmacyPurchaseOrderWithSingleOrder(BaseModel):
    purchase_order: PharmacyPurchaseOrderIn
    single_purchase_order: List[PharmacyPurchaseSingleOrderIn]


class PharmacyPurchaseSingleOrderWithMedicine(PharmacyPurchaseSingleOrderOut):
    medicine_name: Optional[str] = None 
    medicine_generic: Optional[str] = None