from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class NoticeBase(BaseModel):
    cover_img_id:Optional[int] = None
    title: str
    body: str 
    portal: str
    priority: int
    status: bool


class NoticeIn(NoticeBase):
    user_id:int
    cover_img_id:Optional[int] = None
    title: str
    body: str 
    portal: str
    priority: int
    status: bool
    
class NoticeUpdate(NoticeBase):
    cover_img_id: Optional[int] = None
    title: Optional[str] = None
    body: Optional[str] = None 
    portal: Optional[str] = None
    priority: Optional[int] = None
    status: Optional[bool] = None



class NoticeOut(NoticeBase):
    id: int
    user_id: int
    created_at: datetime
    
    class Config:
        orm_mode = True