from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class ImageLogBase(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = None
    service_name: Optional[str] = None
    image_string: Optional[str] = None


class ImageLogIn(ImageLogBase):
    pass


class ImageLogUpdate(ImageLogBase):
    pass


class ImageLogOut(ImageLogBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True