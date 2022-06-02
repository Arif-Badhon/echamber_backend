from datetime import datetime
from pydantic import BaseModel
from typing import Optional

class PdfLogBase(BaseModel):
    user_id: Optional[int] = None
    name: Optional[str] = None
    service_name: Optional[str] = None
    pdf_string: Optional[str] = None


class PdfLogIn(PdfLogBase):
    pass


class PdfLogUpdate(PdfLogBase):
    pass


class PdfLogOut(PdfLogBase):
    id: int
    created_at: datetime

    class Config: 
        orm_mode = True