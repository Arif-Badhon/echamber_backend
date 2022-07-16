from datetime import datetime
from pydantic import BaseModel
from typing import Optional


class ReviewBase(BaseModel):
    service_name: str
    service_id: int
    rating: int
    comment: str
    visible: bool


class ReviewIn(ReviewBase):
    pass


class ReviewWithUser(ReviewIn):
    user_id: int


class ReviewUdate(BaseModel):
    service_name: Optional[str] = None
    service_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None
    visible: Optional[bool] = None


class ReviewOut(BaseModel):
    id: int
    user_id: int
    created_at: datetime
    service_name: Optional[str] = None
    service_id: Optional[int] = None
    rating: Optional[int] = None
    comment: Optional[str] = None
    visible: Optional[bool] = None

    class Config:
        orm_mode = True
