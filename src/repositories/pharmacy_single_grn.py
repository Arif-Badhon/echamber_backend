from repositories import BaseRepo
from models import PharmacySingleGrn
from schemas import PharmacySingleGrnIn, PharmacySingleGrnUpdate

pharmacy_single_grn_repo = BaseRepo[PharmacySingleGrn, PharmacySingleGrnIn, PharmacySingleGrnUpdate](PharmacySingleGrn)