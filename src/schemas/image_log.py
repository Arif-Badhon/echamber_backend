from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ImageLogBase(BaseModel):
    user_id: int
    service_name: str
    image_string: str


class ImageLogIn(ImageLogBase):
    pass


class ImageLogUpdate(BaseModel):
    user_id: Optional[int] = None
    service_name: Optional[str] = None
    image_string: Optional[str] = None


class ImageLogOut(ImageLogBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True