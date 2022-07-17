from datetime import datetime
from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr


class UserBase(BaseModel):
    name: str
    email: Optional[str] = None
    phone: constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )
    sex: str
    is_active: bool


class UserCreate(UserBase):
    password: str
    role_name: str


class UserCreateWitoutRole(UserBase):
    password: str


class UserDBIn(UserBase):
    password: str
    role_id: int


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: Optional[constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )]
    sex: Optional[str]
    role_id: Optional[int]
    is_active: Optional[bool] = True


class UserOut(UserBase):
    id: int
    role_id: int
    created_at: Optional[datetime] = None

    class Config:
        orm_mode = True


class UserOutAuth(UserBase):
    id: int
    role_name: Optional[str]

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    identifier: str
    password: str


class NewPasswordIn(BaseModel):
    password: str
