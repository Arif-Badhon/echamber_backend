from datetime import datetime, date
from pydantic import BaseModel
from typing import List, Optional

class PharmacyGrnBase(BaseModel):
    total_amount_dp: Optional[float] = None
    grn_number: Optional[str] = None
    total_amount_mrp: Optional[float] = None
    total_vat_mrp: Optional[float] = None
    total_discount_mrp: Optional[float] = None
    total_cost_mrp: Optional[float] = None
    pharmaceuticals_name_id: Optional[int] = None
    purchase_order_id: Optional[int] = None
    pharmacy_id: Optional[int] = None
    paid_amount:  Optional[float] = None
    due_amount:  Optional[float] = None


class PharmacyGrnIn(PharmacyGrnBase):
    pass


class PharmacyGrnUpdate(BaseModel):
    total_amount_dp: Optional[float] = None
    grn_number: Optional[str] = None
    total_amount_mrp: Optional[float] = None
    total_vat_mrp: Optional[float] = None
    total_discount_mrp: Optional[float] = None
    total_cost_mrp: Optional[float] = None
    pharmaceuticals_name_id: Optional[int] = None
    purchase_order_id: Optional[int] = None
    pharmacy_id: Optional[int] = None
    paid_amount:  Optional[float] = None
    due_amount:  Optional[float] = None


class PharmacyGrnOut(PharmacyGrnBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# Single Grn


class PharmacySingleGrnBase(BaseModel):
    dp_prize: Optional[float] = None
    quantity: Optional[int] = None
    mrp: Optional[float] = None
    vat: Optional[float] = None
    discount: Optional[float] = None
    cost: Optional[float] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None


class PharmacySingleGrnIn(PharmacySingleGrnBase):
    pass

class PharmacySingleGrnWithGrn(PharmacySingleGrnBase):
    grn_id: int


class PharmacySingleGrnUpdate(BaseModel):
    dp_prize: Optional[float] = None
    quantity: Optional[int] = None
    mrp: Optional[float] = None
    vat: Optional[float] = None
    discount: Optional[float] = None
    cost: Optional[float] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None


class PharmacySingleGrnOut(PharmacySingleGrnBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PharmacyGrnWithSingleGrn(BaseModel):
    grn: PharmacyGrnIn
    single_grn: List[PharmacySingleGrnIn]


class PharmacySingleGrnWithMedicine(PharmacySingleGrnOut):
    medicine_name: Optional[str] = None 
    medicine_generic: Optional[str] = None