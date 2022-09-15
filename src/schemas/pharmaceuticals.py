from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from .users import UserCreateWitoutRole


class PharmaceuticalBase(BaseModel):
    name: str
    established: Optional[str] = None
    details: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    address: Optional[str] = None
    total_generics: Optional[int] = None
    total_brands: Optional[int] = None
    contact_person: Optional[str] = None
    contact_person_phone: Optional[str] = None
    contact_person_email: Optional[str] = None

    class Config:
        orm_mode = True

class PharmaceuticalIn(PharmaceuticalBase):
    pass

class PharmaceuticalUpdate(BaseModel):
    name: Optional[str] = None
    established: Optional[str] = None
    details: Optional[str] = None
    contact_phone: Optional[str] = None
    contact_email: Optional[str] = None
    address: Optional[str] = None
    total_generics: Optional[int] = None
    total_brands: Optional[int] = None
    contact_person: Optional[str] = None
    contact_person_phone: Optional[str] = None
    contact_person_email: Optional[str] = None

    class Config:
        orm_mode = True

class PharmaceuticalOut(PharmaceuticalBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

class PharmaceuticalUserWithPhr(BaseModel):
    pharmaceuticals : PharmaceuticalIn
    user : UserCreateWitoutRole