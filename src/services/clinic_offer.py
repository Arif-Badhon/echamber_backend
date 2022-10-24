from services import BaseService
from models import ClinicOffer
from schemas import ClinicOfferIn, ClinicOfferUpdate
from repositories import clinic_offer_repo


clinic_offer_service = BaseService[ClinicOffer, ClinicOfferIn, ClinicOfferUpdate](ClinicOffer, clinic_offer_repo)