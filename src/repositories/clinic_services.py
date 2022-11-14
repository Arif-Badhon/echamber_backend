from repositories import BaseRepo
from models import ClinicServices
from schemas import ClinicServicesIn, ClinicServicesUpdate
from sqlalchemy.orm import Session


class ClinicServicesRepo(BaseRepo[ClinicServices, ClinicServicesIn, ClinicServicesUpdate]):

    def get_clinic_services_by_clinic_id(self, db: Session, clinic_id: int):
        data =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        return  data


clinic_services_repo = ClinicServicesRepo(ClinicServices)