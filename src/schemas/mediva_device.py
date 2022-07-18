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
