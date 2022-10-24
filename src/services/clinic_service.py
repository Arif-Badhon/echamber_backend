from services import BaseService
from models import ClinicService
from schemas import ClinicServiceIn, ClinicServiceUpdate
from repositories import clinic_service_repo


clinic_service_service = BaseService[ClinicService, ClinicServiceIn, ClinicServiceUpdate](ClinicService, clinic_service_repo)