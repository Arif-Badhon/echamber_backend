from services import BaseService
from models import ClinicActivity
from schemas import ClinicActivityIn, ClinicActivityUpdate
from repositories import clinic_activity_repo


clinic_activity_service = BaseService[ClinicActivity, ClinicActivityIn, ClinicActivityUpdate](ClinicActivity, clinic_activity_repo)
