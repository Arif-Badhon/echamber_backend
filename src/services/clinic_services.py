from services import BaseService
from models import ClinicServices
from schemas import ClinicServicesIn, ClinicServicesUpdate
from repositories import clinic_service_repo


clinic_service_service = BaseService[ClinicServices, ClinicServicesIn, ClinicServicesUpdate](ClinicServices, clinic_service_repo)