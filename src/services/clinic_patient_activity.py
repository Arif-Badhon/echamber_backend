from services import BaseService
from models import ClinicPatientActivity
from schemas import ClinicPatientActivityIn, ClinicPatientActivityUpdate
from repositories import clinic_patient_activity_repo


clinic_patient_activity_service = BaseService[ClinicPatientActivity, ClinicPatientActivityIn, ClinicPatientActivityUpdate](ClinicPatientActivity, clinic_patient_activity_repo)