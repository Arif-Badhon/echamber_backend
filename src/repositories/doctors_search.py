from __future__ import division
from unicodedata import name
from sqlalchemy.orm import Session
from sqlalchemy.sql import alias
from models import User, UserDetail, DoctorQualification, DoctorSpeciality, DoctorChamber
from repositories import BaseRepo
from schemas import UserBase, UserUpdate

# Base class not inheritade...


class DoctorsSearchRepo(BaseRepo[User, UserBase, UserUpdate]):

    def doctor_search(self, db: Session, district: str, speciality: str, name: str, skip: int, limit: int):

        data = db.query(
            DoctorChamber, DoctorSpeciality, User).join(
            DoctorChamber, DoctorChamber.user_id == User.id).join(DoctorSpeciality, DoctorSpeciality.user_id == User.id).filter(
            DoctorChamber.district.like(f"%{district}%")).filter(User.name.like(f"%{name}%")).filter(DoctorSpeciality.speciality.like(f"%{speciality}%")).offset(skip).limit(limit).all()
        return data


doctors_search_repo = DoctorsSearchRepo(User)


# district
# speciality
# name
