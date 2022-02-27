from schemas import DoctorIn, DoctorUpdate
from models import Doctor
from services import BaseService
from repositories import doctors_repo

doctors_service = BaseService[Doctor, DoctorIn,
                              DoctorUpdate](Doctor, doctors_repo)
