from services import BaseService
from repositories import doctor_workplace_repo
from models import DoctorWorkPlace
from schemas import DoctorWorkPlaceIn, DoctorWorkPlaceUpdate

doctor_workplace_service = BaseService[DoctorWorkPlace, DoctorWorkPlaceIn, DoctorWorkPlaceUpdate](DoctorWorkPlace, doctor_workplace_repo)
