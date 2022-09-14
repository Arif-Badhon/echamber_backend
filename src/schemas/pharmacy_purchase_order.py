from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class PharmacyPurchaseOrderBase(BaseModel):
    total_amount_dp: Optional[float] = None
    discount = Optional[float] = None
    payable_amount:Optional[float] = None
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
    remarks: Optional[str] = None

class PharmacyPurchaseOrderOut(PharmacyPurchaseOrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

