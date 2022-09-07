from repositories import BaseRepo
from models import Pharmacy
from schemas import PharmacyIn, PharmacyUpdate

pharmacy_repo = BaseRepo[Pharmacy, PharmacyIn, PharmacyUpdate](Pharmacy)