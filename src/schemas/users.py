from typing import Optional
from pydantic import BaseModel
from pydantic.types import constr


class UserBase(BaseModel):
    name: str
    email: str
    phone: constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )
    sex: str
    is_active: bool


class UserCreate(UserBase):
    password: str
    role_name: str


class UserDBIn(UserBase):
    password: str
    role_id: int


class UserUpdate(BaseModel):
    name: Optional[str]
    email: Optional[str]
    phone: constr(
        min_length=11, max_length=14, regex=r"(\+880)?[0-9]{11}"
    )
    sex: Optional[str]


class UserOut(UserBase):
    role_id: int

    class Config:
        orm_mode = True


class UserLogin(BaseModel):
    identifier: str
    password: str


class NewPasswordIn(BaseModel):
    password: str
