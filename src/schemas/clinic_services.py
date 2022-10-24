from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClinicServicesBase(BaseModel):
    clinic_id: int
    servive_name: Optional[str] = None
    service_details: Optional[str] = None
    service_price: Optional[float] = None
    image_id: Optional[int] = None


class ClinicServicesIn(ClinicServicesBase):
    pass


class ClinicServicesUpdate(BaseModel):
    servive_name: Optional[str] = None
    service_details: Optional[str] = None
    service_price: Optional[float] = None
    image_id: Optional[int] = None

class ClinicServicesOut(ClinicServicesBase):
    id: int
    created_at: datetime

    class Confifg:
        orm_mode = True