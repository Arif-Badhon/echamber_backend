from services import BaseService
from models import ClinicDetails
from schemas import ClinicDetailsIn, ClinicDetailsUpdate
from repositories import clinic_details_repo

clinic_details_service = BaseService[ClinicDetails, ClinicDetailsIn, ClinicDetailsUpdate](ClinicDetails, clinic_details_repo)