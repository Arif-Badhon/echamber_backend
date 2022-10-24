from repositories import BaseRepo
from models import ClinicServices
from schemas import ClinicServicesIn, ClinicServicesUpdate


clinic_service_repo = BaseRepo[ClinicServices, ClinicServicesIn, ClinicServicesUpdate](ClinicServices)