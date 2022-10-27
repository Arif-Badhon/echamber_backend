from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClinicOfferBase(BaseModel):
    clinic_id: int
    offer_name: Optional[str] = None
    offer_details: Optional[str] = None
    offer_price: Optional[float] = None
    image_id: Optional[int] = None


class ClinicOfferIn(ClinicOfferBase):
    pass


class ClinicOfferUpdate(BaseModel):
    offer_name: Optional[str] = None
    offer_details: Optional[str] = None
    offer_price: Optional[float] = None
    image_id: Optional[int] = None

class ClinicOfferOut(ClinicOfferBase):
    id: int
    created_at: datetime

    class Confifg:
        orm_mode = True