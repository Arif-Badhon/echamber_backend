from repositories import BaseRepo
from models import ClinicDetails
from schemas import ClinicDetailsIn, ClinicDetailsUpdate
from sqlalchemy.orm import Session

class ClinicDetailsRepo(BaseRepo[ClinicDetails, ClinicDetailsIn, ClinicDetailsUpdate]):
    
    def get_details_by_clinic_id(self, db: Session, clinic_id: int):
        data =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        return  data

clinic_details_repo = ClinicDetailsRepo(ClinicDetails)