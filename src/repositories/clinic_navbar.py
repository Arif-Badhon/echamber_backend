from repositories import BaseRepo
from models import ClinicNavbar
from schemas import ClinicNavbarIn, ClinicDetailsUpdate
from sqlalchemy.orm import Session


class ClinicNavbarRepo(BaseRepo[ClinicNavbar, ClinicNavbarIn, ClinicDetailsUpdate]):
    def get_nav_by_clinic_id(self, db: Session, clinic_id: int):
        data =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        return  data

clinic_navbar_repo = ClinicNavbarRepo(ClinicNavbar)