from pydantic import BaseModel
from .doctors import DoctorOut
from .users import UserOut


class UserDoctorOut(BaseModel):
    User: UserOut
    Doctor: DoctorOut

    class Config:
        orm_mode = True
