from typing import Optional
from pydantic import BaseModel
from datetime import datetime, date

class PharmacyEverySingleStockBase(BaseModel):
    quantity: Optional[int] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None
    single_grn: Optional[int] = None


class PharmacyEverySingleStockIn(PharmacyEverySingleStockBase):
    pass

class PharmacyStockWithPharmacyID(PharmacyEverySingleStockBase):
    pharmacy_id: int


class PharmacyEverySingleStockUpdate(BaseModel):
    quantity: Optional[int] = None
    expiry_date: Optional[date] = None
    batch_number: Optional[str] = None
    medicine_id: Optional[int] = None
    single_grn: Optional[int] = None

class PharmacyEverySingleStockOut(PharmacyEverySingleStockBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Total current Stock

class PharmacyTotalCurrentStockBase(BaseModel):
     quantity: Optional[int] = None
     medicine_id: Optional[int] = None
     Pharmacy_id: Optional[int] = None


class PharmacyTotalCurrentStockIn(PharmacyTotalCurrentStockBase):
    pass


class PharmacyTotalCurrentStockUpdate(BaseModel):
     quantity: Optional[int] = None
     medicine_id: Optional[int] = None


class PharmacyTOtalCurrentStockOut(PharmacyTotalCurrentStockBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True