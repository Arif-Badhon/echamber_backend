from repositories import BaseRepo
from models import ClinicUser
from schemas import ClinicUserIn, ClinicUserUpdate


clinic_user_repo = BaseRepo[ClinicUser, ClinicUserIn, ClinicUserUpdate](ClinicUser)