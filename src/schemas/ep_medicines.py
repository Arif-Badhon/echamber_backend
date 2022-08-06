from datetime import datetime
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


class MedicineInWithUser(MedicineBase):
    add_status: str
    added_by_id: int


class MedicineUpdate(MedicineBase):
    add_status: Optional[str] = None
    added_by_id: Optional[int] = None


class MedicineOut(MedicineBase):
    id: int
    add_status: Optional[str] = None
    added_by_id: Optional[int] = None
    created_at: datetime

    class Config:
        orm_mode = True


# for ep medicines

class EpMedicineBase(BaseModel):
    name: str
    generic: str
    pharmaceuticals: str
    form: str
    strength: str
    doses: str
    after_meal: bool
    days: int
    remarks: str


class EpMedicineIn(EpMedicineBase):
    pass


class EpMedicineWithEp(EpMedicineBase):
    ep_id: int


class EpMedicineUpdate(BaseModel):
    name: Optional[str] = None
    generic: Optional[str] = None
    pharmaceuticals: Optional[str] = None
    form: Optional[str] = None
    strength: Optional[str] = None
    doses: Optional[str] = None
    after_meal: Optional[bool] = None
    days: Optional[int] = None
    remarks: Optional[str] = None


class EpMedicineOut(BaseModel):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True


class EpPharmaOut(BaseModel):
    pharmaceuticals: str

    class Config:
        orm_mode = True
