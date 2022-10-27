from services import BaseService
from models import ClinicNavbar
from schemas import ClinicNavbarIn, ClinicNavbarUpdate
from repositories import clinic_navbar_repo


clinic_navbar_service = BaseService[ClinicNavbar, ClinicNavbarIn, ClinicNavbarUpdate](ClinicNavbar, clinic_navbar_repo)