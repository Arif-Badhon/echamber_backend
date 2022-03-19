from pydantic import BaseModel


class CcBase(BaseModel):
    cc: str


class CcIn(CcBase):
    pass


class CcUpdate(CcBase):
    pass


class CcOut(BaseModel):
    id: int
    cc: str

    class Config:
        orm_mode = True
