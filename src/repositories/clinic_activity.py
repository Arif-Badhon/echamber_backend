from repositories import BaseRepo
from models import ClinicActivity
from schemas import ClinicActivityIn, ClinicActivityUpdate

clinic_activity_repo = BaseRepo[ClinicActivity, ClinicActivityIn, ClinicActivityUpdate](ClinicActivity)