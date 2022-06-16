from typing import Optional
from pydantic import BaseModel


class MedicineBase(BaseModel):
    name: str
    generic: str
    form: str
    strength: str
    pharmaceuticals: str
    unit_type: Optional[str] = None
    unit_price: Optional[float] = None


class MedicineIn(MedicineBase):
    pass


class MedicineUpdate(MedicineBase):
    pass


class MedicineOut(MedicineBase):
    id: int

    class Config:
        orm_mode = True
