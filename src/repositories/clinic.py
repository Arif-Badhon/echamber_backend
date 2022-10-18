from repositories import BaseRepo
from models import Clinic
from schemas import ClinicIn, ClinicUpdate


clinic_repo = BaseRepo[Clinic, ClinicIn, ClinicUpdate](Clinic)