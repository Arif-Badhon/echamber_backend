from repositories import BaseRepo
from models import PharmacyGrn
from schemas import PharmacyGrnIn, PharmacyGrnUpdate

pharmacy_grn_repo = BaseRepo[PharmacyGrn, PharmacyGrnIn, PharmacyGrnUpdate](PharmacyGrn)