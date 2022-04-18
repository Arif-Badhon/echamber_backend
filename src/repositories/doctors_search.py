from sqlalchemy.orm import Session
from models import User, UserDetail, DoctorQualification, DoctorSpeciality, DoctorChamber
from repositories import BaseRepo
from schemas import UserBase, UserUpdate

# Base class not inheritade...


class DoctorsSearchRepo(BaseRepo[User, UserBase, UserUpdate]):

    def doctor_search(self, db: Session, search_key: str, skip: int = 0, limit: int = 10):
        query = db.query(self.model, UserDetail).select_from(self.model).join(UserDetail).filter(self.model.name.like(
            f"%{search_key}%") | UserDetail.division.like(f"%{search_key}%") | UserDetail.district.like(f"{search_key}")).offset(skip).limit(limit).all()
        return query


doctors_search_repo = DoctorsSearchRepo(User)

#    UserDetail.division.like(f"%{search_key}%") |
#    UserDetail.district.like(f"%{search_key}%") |
#    DoctorQualification.qualification.like(f"%{search_key}%") |
#    DoctorSpeciality.speciality.like(f"%{search_key}%") |
#    DoctorChamber.detail.like(f"%{search_key}%"
