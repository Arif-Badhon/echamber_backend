from pydantic import BaseModel


class MedicineBase(BaseModel):
    name: str
    generic: str
    form: str
    strength: str
    pharmaceuticals: str


class MedicineIn(MedicineBase):
    pass


class MedicineUpdate(MedicineBase):
    pass


class MedicineOut(MedicineBase):
    id: int

    class Config:
        orm_mode = True
