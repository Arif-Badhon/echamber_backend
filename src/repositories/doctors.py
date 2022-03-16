from repositories.base import BaseRepo
from models import Doctor
from schemas import DoctorIn, DoctorUpdate


doctors_repo = BaseRepo[Doctor, DoctorIn, DoctorUpdate](Doctor)
