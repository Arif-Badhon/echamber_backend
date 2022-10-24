from repositories import BaseRepo
from models import ClinicOffer
from schemas import ClinicOfferIn, ClinicOfferUpdate


clinic_offer_repo = BaseRepo[ClinicOffer, ClinicOfferIn, ClinicOfferUpdate](ClinicOffer)