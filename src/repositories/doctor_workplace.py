from repositories import BaseRepo
from models import DoctorWorkPlace
from schemas import DoctorWorkPlaceIn, DoctorWorkPlaceUpdate

doctor_workplace_repo = BaseRepo[DoctorWorkPlace, DoctorWorkPlaceIn, DoctorWorkPlaceUpdate](DoctorWorkPlace)
