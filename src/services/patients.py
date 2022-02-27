from repositories import patients_repo
from models import Patient
from schemas import PatientIn, PatientUpdate
from services import BaseService

patients_service = BaseService[Patient, PatientIn,
                               PatientUpdate](Patient, patients_repo)
