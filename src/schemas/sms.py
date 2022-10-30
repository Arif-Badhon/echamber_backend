from pydantic import BaseModel


# ServiceClassSendTextMessage(String Username, String Password, String
# From, String To, String Message)


class SmsBase(BaseModel):
    username: str
    password: str
    sms_from: str
    sms_to: str
    sms: str


class SmsIn(SmsBase):
    pass


class SmsOut(BaseModel):
    pass

    class Config:
        orm_mode = True
