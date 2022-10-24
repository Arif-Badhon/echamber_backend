from repositories import BaseRepo
from models import ClinicService
from schemas import ClinicServiceIn, ClinicServiceUpdate


clinic_service_repo = BaseRepo[ClinicService, ClinicServiceIn, ClinicServiceUpdate](ClinicService)