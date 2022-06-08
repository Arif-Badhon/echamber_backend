from pydantic import BaseModel


class CcBase(BaseModel):
    chief_complaints: str


class CcIn(CcBase):
    pass


class CcUpdate(CcBase):
    pass


class CcOut(BaseModel):
    id: int
    chief_complaints: str

    class Config:
        orm_mode = True
