from repositories import BaseRepo
from models import ClinicDetails
from schemas import ClinicDetailsIn, ClinicDetailsUpdate

clinic_details_repo = BaseRepo[ClinicDetails, ClinicDetailsIn, ClinicDetailsUpdate](ClinicDetails)