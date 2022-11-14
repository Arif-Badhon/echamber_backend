from repositories import BaseRepo
from models import ClinicOffer
from schemas import ClinicOfferIn, ClinicOfferUpdate
from sqlalchemy.orm import Session

class ClinicOfferRepo(BaseRepo[ClinicOffer, ClinicOfferIn, ClinicOfferUpdate]):

    def get_clinic_offer_by_clinic_id(self, db: Session, clinic_id: int):
        data =  db.query(self.model).filter(self.model.clinic_id == clinic_id).all()
        return  data


clinic_offer_repo = ClinicOfferRepo(ClinicOffer)