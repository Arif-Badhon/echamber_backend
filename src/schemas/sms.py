import typing
from pydantic import BaseModel
from typing import Optional

# ServiceClassSendTextMessage(String Username, String Password, String
# From, String To, String Message)


class SmsBase(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None
    sms_from: Optional[str] = None
    sms_to: Optional[str] = None
    sms: Optional[str] = None


class SmsIn(SmsBase):
    pass


class SmsOut(BaseModel):
    pass

    class Config:
        orm_mode = True
