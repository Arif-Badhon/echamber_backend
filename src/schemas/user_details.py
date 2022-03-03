from datetime import date
from typing import Optional
from pydantic import BaseModel


class UserDetailBase(BaseModel):
    country: Optional[str]
    division: Optional[str]
    district: Optional[str]
    post_code: Optional[str]
    sub_district: Optional[str]
    nid: Optional[str]
    dob: Optional[date]
    blood_group: Optional[str]


class UserDetailIn(UserDetailBase):
    user_id: int


class UserDetailUpdate(UserDetailBase):
    pass


class UserDetailOut(UserDetailBase):
    user_id: Optional[int]

    class Config:
        orm_mode = True
