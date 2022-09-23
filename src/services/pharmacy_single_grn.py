from services import BaseService
from models import PharmacySingleGrn
from schemas import PharmacySingleGrnIn, PharmacySingleGrnUpdate
from repositories import pharmacy_single_grn_repo

pharmacy_single_grn_service = BaseService[PharmacySingleGrn, PharmacySingleGrnIn, PharmacySingleGrnUpdate](PharmacySingleGrn, pharmacy_single_grn_repo)