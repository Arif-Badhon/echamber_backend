from pydantic import BaseModel


class AdviceBase(BaseModel):
    advice: str


class AdviceIn(AdviceBase):
    pass


class AdviceUpdate(AdviceBase):
    pass


class AdviceOut(AdviceBase):
    id: int
    advice: str

    class Config:
        orm_mode = True
