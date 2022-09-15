from datetime import datetime
from pydantic import BaseModel

class PharmaecuticalsUserBase(BaseModel):
    user_id = int

class PharmaecuticalsUserIn(PharmaecuticalsUserBase):
    pass

class PhamaceuticalsUserWithPhrId(PharmaecuticalsUserBase):
    phr_id = int

class PharmaecuticalsUserUpdate(BaseModel):
    user_id = int 

class PharmaecuticalsUserOut(PharmaecuticalsUserBase):
    id: int
    user_id = int
    phr_id = int
    created_at: datetime

    class Confic:
        orm_mode = True

