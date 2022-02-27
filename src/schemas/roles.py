from pydantic import BaseModel
from typing import Optional


class RoleIn(BaseModel):
    name: str


class RoleUpdate(BaseModel):
    name: Optional[str]

    class Config:
        orm_mode = True


class RoleOut(BaseModel):
    id: Optional[int]
    name: Optional[str]

    class Config:
        orm_mode = True
