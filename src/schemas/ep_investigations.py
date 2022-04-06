from pydantic import BaseModel


class InvBase(BaseModel):
    investigation: str


class InvIn(InvBase):
    pass


class InvUpdate(InvBase):
    pass


class InvOut(InvBase):
    id: int
    investigation: str

    class Config:
        orm_mode = True
