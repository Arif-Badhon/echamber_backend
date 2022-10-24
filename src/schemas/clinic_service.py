from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClinicServiceBase(BaseModel):
    clinic_id: int
    servive_name: Optional[str] = None
    service_details: Optional[str] = None
    service_price: Optional[float] = None
    image_id: Optional[int] = None


class ClinicServiceIn(ClinicServiceBase):
    pass


class ClinicServiceUpdate(BaseModel):
    servive_name: Optional[str] = None
    service_details: Optional[str] = None
    service_price: Optional[float] = None
    image_id: Optional[int] = None

class ClinicServiceOut(ClinicServiceBase):
    id: int
    created_at: datetime

    class Confifg:
        orm_mode = True