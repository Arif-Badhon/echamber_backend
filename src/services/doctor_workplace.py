from services import BaseService
from repositories import doctor_workplace_repo
from models import DoctorWorkPlace
from schemas import DoctorWorkPlaceIn, DoctorWorkPlaceUpdate


class DoctorWorkPlaceService(BaseService[DoctorWorkPlace, DoctorWorkPlaceIn, DoctorWorkPlaceUpdate]):
    pass


doctor_workplace_service = DoctorWorkPlaceService(DoctorWorkPlace, doctor_workplace_repo)
