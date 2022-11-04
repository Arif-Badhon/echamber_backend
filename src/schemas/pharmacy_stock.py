from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class PharmacyEverySingleStockBase(BaseModel):
    quantity: Optional[int] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None


class PharmacyEverySingleStockIn(PharmacyEverySingleStockBase):
    pass

class PharmacySingleGrnForStock(PharmacyEverySingleStockIn):
    single_grn_id: int
    pharmacy_id: int


class PharmacyEverySingleStockUpdate(BaseModel):
    quantity: Optional[int] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None
    single_grn_id: Optional[int] = None

class PharmacyEverySingleStockOut(PharmacyEverySingleStockBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PharmacyEverySingleStockOutWithMedicine(PharmacyEverySingleStockOut):
    pharmacy_id: Optional[int] = None
    medicine_name: Optional[str] = None 
    medicine_generic: Optional[str] = None
    medicine_strength: Optional[str] = None
    pharmaceuticals: Optional[str] = None


# Total current Stock

class PharmacyTotalCurrentStockBase(BaseModel):
     quantity: Optional[int] = None
     medicine_id: Optional[int] = None
     pharmacy_id: Optional[int] = None


class PharmacyTotalCurrentStockIn(PharmacyTotalCurrentStockBase):
    pass


class PharmacyTotalCurrentStockUpdate(BaseModel):
     quantity: Optional[int] = None


class PharmacyTotalCurrentStockOut(PharmacyTotalCurrentStockBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


class PharmacyTotalCurrentStockWithMedicine(PharmacyTotalCurrentStockOut):
    medicine_name: Optional[str] = None 
    medicine_generic: Optional[str] = None
    medicine_strength: Optional[str] = None
    pharmaceuticals: Optional[str] = None