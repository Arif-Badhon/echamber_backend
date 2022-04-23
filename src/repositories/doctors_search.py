from __future__ import division
from unicodedata import name
from sqlalchemy.orm import Session
from models import User, UserDetail, DoctorQualification, DoctorSpeciality, DoctorChamber
from repositories import BaseRepo
from schemas import UserBase, UserUpdate

# Base class not inheritade...


class DoctorsSearchRepo(BaseRepo[User, UserBase, UserUpdate]):

    def doctor_search(self, db: Session, name: str, speciality: str, skip: int = 0, limit: int = 10):
        query =  db.query(self.model, DoctorSpeciality).join(DoctorSpeciality).filter(self.model.name.like(f"%{name}%")).filter(DoctorSpeciality.speciality.like(f"%{speciality}%")).all()        
        return query


doctors_search_repo = DoctorsSearchRepo(User)


# name
# speciality
# division
# district