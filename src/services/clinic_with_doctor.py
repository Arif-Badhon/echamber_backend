from services import BaseService
from models import ClinicWithDoctor
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate
from repositories import clinic_with_doctor_repo


clinic_with_doctor_service = BaseService[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate](ClinicWithDoctor, clinic_with_doctor_repo)
