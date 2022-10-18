from services import BaseService
from models import ClinicUser
from schemas import ClinicUserIn, ClinicUserUpdate
from repositories import clinic_user_repo


clinic_user_service = BaseService[ClinicUser, ClinicUserIn, ClinicUserUpdate](ClinicUser, clinic_user_repo)