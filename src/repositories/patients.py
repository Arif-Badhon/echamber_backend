from models import Patient
from repositories import BaseRepo
from schemas import PatientIn, PatientUpdate

patients_repo = BaseRepo[Patient, PatientIn, PatientUpdate](Patient)
