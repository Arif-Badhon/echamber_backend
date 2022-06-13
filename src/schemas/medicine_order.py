from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class MedicineOrderBase(BaseModel):
    name: Optional[str] = None
    generic: Optional[str] = None
    form: Optional[str] = None
    strength: Optional[str] = None
    pharmaceuticals: Optional[str] = None
    quantity: Optional[int] = None
    unit_price_tp: Optional[int] = None
    unit_price_mrp: Optional[int] = None
    unit_discount_percent: Optional[int] = None
    total: Optional[int] = None


class MedicineOrderIn(MedicineOrderBase):
    name: Optional[str] = None
    generic: Optional[str] = None
    form: Optional[str] = None
    strength: Optional[str] = None
    pharmaceuticals: Optional[str] = None
    quantity: Optional[int] = None
    unit_price_tp: Optional[int] = None
    unit_price_mrp: Optional[int] = None
    unit_discount_percent: Optional[int] = None
    total: Optional[int] = None

class MedicineOrderInWithService(MedicineOrderBase):
    service_order_id: Optional[int] = None
    name: Optional[str] = None
    generic: Optional[str] = None
    form: Optional[str] = None
    strength: Optional[str] = None
    pharmaceuticals: Optional[str] = None
    quantity: Optional[int] = None
    unit_price_tp: Optional[int] = None
    unit_price_mrp: Optional[int] = None
    unit_discount_percent: Optional[int] = None
    total: Optional[int] = None


class MedicineOrderUpdate(MedicineOrderBase):
    pass


class MedicineOrderOut(MedicineOrderBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True