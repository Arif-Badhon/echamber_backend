from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ClinicDetailsBase(BaseModel):
    clinic_id: int
    title: Optional[str] = None
    sub_title: Optional[str] = None
    title_bg_image_id: Optional[int] = None
    about: Optional[str] = None
    about_image_id: Optional[int] = None
    contuct_us: Optional[str] = None
    footer: Optional[str] = None


class ClinicDetailsIn(ClinicDetailsBase):
    pass


class ClinicDetailsUpdate(BaseModel):
    title: Optional[str] = None
    sub_title: Optional[str] = None
    title_bg_image_id: Optional[int] = None
    about: Optional[str] = None
    about_image_id: Optional[int] = None
    contuct_us: Optional[str] = None
    footer: Optional[str] = None

class ClinicDetailsOut(ClinicDetailsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True