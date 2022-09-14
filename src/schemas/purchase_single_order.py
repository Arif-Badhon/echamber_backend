from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PurchaseSingleOrderBase(BaseModel):
    quantity: Optional[int] = None
    unit_price_dp: Optional[float] = None
    discount: Optional[float] = None
    payable_prize_dp: Optional[float] = None
    purchase_id: Optional[int] = None
    medicine_id: Optional[int] = None

class PurchaseSingleOrderIn(PurchaseSingleOrderBase):
    pass 

class PurchaseSingleOrderUpdate(BaseModel):
    pass 

class PharmacySingleOrderOut(PurchaseSingleOrderBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True