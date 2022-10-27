from repositories import BaseRepo
from models import ClinicNavbar
from schemas import ClinicNavbarIn, ClinicDetailsUpdate

clinic_navbar_repo = BaseRepo[ClinicNavbar, ClinicNavbarIn, ClinicDetailsUpdate](ClinicNavbar)