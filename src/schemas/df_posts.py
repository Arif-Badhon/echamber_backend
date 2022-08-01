from datetime import datetime
from pydantic import BaseModel
from typing import Optional


# catagory schema

class DfPostCatagoryBase(BaseModel):
    name: str
    details: Optional[str] = None


class DfPostCatagoryIn(DfPostCatagoryBase):
    pass


class DfPostCatagoryUpdate(DfPostCatagoryBase):
    pass


class DfPostCatagoryOut(DfPostCatagoryBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# tag schema

class DfPostTagBase(BaseModel):
    user_id: int
    tag: str


class DfPostTagIn(DfPostTagBase):
    pass


class DfPostTagUpdate(BaseModel):
    user_id: Optional[int] = None
    tag: Optional[str] = None


class DfPostTagOut(DfPostTagBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True


# tag relation schema

class DfPostTagRelationBase(BaseModel):
    post_id: int
    tag_id: int


class DfPostTagIn(DfPostTagRelationBase):
    pass


class DfPostTagUpdate(BaseModel):
    post_id: Optional[int] = None
    tag_id: Optional[int] = None


class DfPostTagOut(DfPostTagRelationBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True

# post relation


class DfPostBase(BaseModel):
    title: str
    body: str
    user_id: int
    catagory_id: int
    cover_image_id: Optional[int] = None


class DfPostIn(DfPostBase):
    pass


class DfPostUpdate(BaseModel):
    title: Optional[str] = None
    body: Optional[str] = None
    user_id: Optional[int] = None
    catagory_id: Optional[int] = None
    cover_image_id: Optional[int] = None


class DfPostOut(DfPostBase):
    id: int
    cover_image_str: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
