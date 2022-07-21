from unicodedata import name
from sqlalchemy.orm import Session
from models import User, UserDetail, DoctorQualification, DoctorSpeciality, DoctorChamber, Role
from repositories import BaseRepo
from schemas import UserBase, UserUpdate
from .roles import roles_repo


# Base class not inheritade...


class DoctorsSearchRepo(BaseRepo[User, UserBase, UserUpdate]):

    def doc_search_by_chamber_loc(self, db: Session, skip: int, limit: int, district: str):
        data = db.query(User).join(DoctorChamber, DoctorChamber.user_id == User.id).filter(DoctorChamber.district.like(f"%{district}%")).offset(skip).limit(limit).all()
        return data

    def doc_search_by_speciality(self, db: Session, skip: int, limit: int, speciality: str):
        data = db.query(User).join(DoctorSpeciality, DoctorSpeciality.user_id == User.id).filter(DoctorSpeciality.speciality.like(f"%{speciality}%")).offset(skip).limit(limit).all()
        return data

    def doc_search_by_name(self, db: Session, skip: int, limit: int, name: str):
        role_id = roles_repo.search_name_id(db=db, name='doctor')
        data = db.query(self.model).filter(self.model.role_id == role_id).filter(self.model.name.like(f"%{name}%")).offset(skip).limit(limit).all()
        return data


doctors_search_repo = DoctorsSearchRepo(User)


# district
# speciality
# name
