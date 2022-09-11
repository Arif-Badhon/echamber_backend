from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class PharmacyPurchaseOrderBase(BaseModel):
    total_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    due_amount: Optional[float] = None
    remarks: Optional[str] = None
    purchase_number: Optional[str] = None
    pharmaceuticals_id: Optional[int] = None
    user_id: Optional[int] = None
    pharmacy_id: Optional[int] = None

class PharmacyPurchaseOrderIn(PharmacyPurchaseOrderBase):
    pass

class PharmacyPurchaseOrderUpdate(BaseModel):
    remarks: Optional[str] = None

class PharmacyPurchaseOrderOut(PharmacyPurchaseOrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

