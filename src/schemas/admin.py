from pydantic import BaseModel
from .doctors import DoctorOut
from .users import UserOut
from .doctor_qualifications import DoctorQualificationOut
from .doctor_specialities import DoctorSpecialityOut

class UserDoctorOut(BaseModel):
    User: UserOut
    Doctor: DoctorOut
    DoctorQualification: DoctorQualificationOut
    DoctorSpeciality: DoctorSpecialityOut

    class Config:
        orm_mode = True
