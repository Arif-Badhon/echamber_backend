from repositories import BaseRepo
from models import ClinicWithDoctor
from schemas import ClinicWithDoctorIn, ClinicWithDoctorUpdate


clinic_with_doctor_repo = BaseRepo[ClinicWithDoctor, ClinicWithDoctorIn, ClinicWithDoctorUpdate](ClinicWithDoctor)