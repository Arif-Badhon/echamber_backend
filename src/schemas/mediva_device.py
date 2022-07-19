from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# Catagory

class MedivaDeviceCatagoryBase(BaseModel):
    name: Optional[str] = None
    details: Optional[str] = None


class MedivaDeviceCatagoryIn(MedivaDeviceCatagoryBase):
    pass


class MedivaDeviceCatagoryUpdate(MedivaDeviceCatagoryBase):
    pass


class MedivaDeviceCatagoryOut(MedivaDeviceCatagoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# Device
class MedivaDeviceBase(BaseModel):
    name: str
    brand: Optional[str] = None
    model: Optional[str] = None
    details: Optional[str] = None
    img_id: Optional[int] = None
    catagory_id: int
    quantity: int
    trp: Optional[int] = None
    old_mrp: Optional[int] = None
    current_mrp: int


class MedivaDeviceIn(MedivaDeviceBase):
    pass


class MedivaDeviceUpdate(BaseModel):
    name: Optional[str] = None
    brand: Optional[str] = None
    model: Optional[str] = None
    details: Optional[str] = None
    img_id: Optional[int] = None
    catagory_id: Optional[int] = None
    quantity: Optional[int] = None
    trp: Optional[int] = None
    old_mrp: Optional[int] = None
    current_mrp: Optional[int] = None


class MedivaDeviceOut(MedivaDeviceBase):
    pass

    class Config:
        orm_mode = True
