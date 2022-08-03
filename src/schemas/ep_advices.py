from datetime import datetime
from pydantic import BaseModel

# advice list


class AdviceBase(BaseModel):
    advice: str


class AdviceIn(AdviceBase):
    pass


class AdviceUpdate(AdviceBase):
    pass


class AdviceOut(AdviceBase):
    id: int

    class Config:
        orm_mode = True


# advice for ep

class AdviceInWithEp(AdviceBase):
    ep_id: int


class AdviceOutWithEp(AdviceBase):
    id: int
    ep_id: int
    created_at: datetime

    class Config:
        orm_mode = True
