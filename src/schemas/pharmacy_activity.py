from pydantic import BaseModel
from datetime import datetime
from typing import Optional
from .users import UserOut
from .user_details import UserDetailOut


class PharmacyActivityBase(BaseModel):
    pharmacy_id: int
    user_id: int
    service_name: str
    service_received_id: int
    remark: Optional[str] = None


class PharmacyActivityIn(PharmacyActivityBase):
    pass


class PharmacyActivityUpdate(BaseModel):
    pass


class PharmacyActivityOut(PharmacyActivityBase):
    created_at: datetime

    class Config:
        orm_mode = True


class PharmacyActivityOutWithUser(BaseModel):
    PharmacyActivity: PharmacyActivityOut
    User: UserOut
    UserDetail: UserDetailOut