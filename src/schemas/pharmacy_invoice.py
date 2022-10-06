from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class PharmacyInvoiceBase(BaseModel):
    subtotal_amount: Optional[float] = None
    total_amount_mrp: Optional[float] = None
    total_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    due_amount: Optional[float] = None
    remarks: Optional[str] = None
    discount: Optional[float] = None
    vat: Optional[float] = None
    invoice_number: Optional[str] = None
    customer_id: Optional[int] = None
    pharmacy_id: Optional[int] = None


class PharmacyInvoiceIn(PharmacyInvoiceBase):
    pass


class PharmacyInvoiceUpdate(BaseModel):
    subtotal_amount: Optional[float] = None
    total_amount_mrp: Optional[float] = None
    total_amount: Optional[float] = None
    paid_amount: Optional[float] = None
    due_amount: Optional[float] = None
    remarks: Optional[str] = None
    discount: Optional[float] = None
    vat: Optional[float] = None
    invoice_number: Optional[str] = None
    customer_id: Optional[int] = None
    pharmacy_id: Optional[int] = None
    

class PharmacyInvoiceOut(PharmacyInvoiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Pharmacy Single Invoice

class PharmacySingleInvoiceBase(BaseModel):
    mrp: Optional[float] = None
    quantity: Optional[int] = None
    unit_prize: Optional[float] = None
    discount: Optional[float] = None
    cost: Optional[float] = None
    medicine_id: Optional[int] = None
    invoice_id: Optional[int] = None


class PharmacySingleInvoiceIn(PharmacySingleInvoiceBase):
    pass 


class PharmacySingleInvoiceUpdate(BaseModel):
    mrp: Optional[float] = None
    quantity: Optional[int] = None
    unit_prize: Optional[float] = None
    discount: Optional[float] = None
    cost: Optional[float] = None
    medicine_id: Optional[int] = None
    invoice_id: Optional[int] = None


class PharmacySingleInvoiceOut(PharmacySingleInvoiceBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True