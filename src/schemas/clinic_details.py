from pydantic import BaseModel
from datetime import datetime, time
from typing import Optional

class ClinicDetailsBase(BaseModel):
    clinic_id: int
    logo_image_id: Optional[int]
    title: Optional[str] = None
    sub_title: Optional[str] = None
    title_bg_image_id: Optional[int] = None
    about: Optional[str] = None
    about_image_id: Optional[int] = None
    contact_us: Optional[str] = None
    starting_time: Optional[time] = None
    ending_time: Optional[time] = None
    footer: Optional[str] = None


class ClinicDetailsIn(ClinicDetailsBase):
    pass


class ClinicDetailsUpdate(BaseModel):
    logo_image_id: Optional[int]
    title: Optional[str] = None
    sub_title: Optional[str] = None
    title_bg_image_id: Optional[int] = None
    about: Optional[str] = None
    about_image_id: Optional[int] = None
    contact_us: Optional[str] = None
    starting_time: Optional[time] = None
    ending_time: Optional[time] = None
    footer: Optional[str] = None

class ClinicDetailsOut(ClinicDetailsBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True