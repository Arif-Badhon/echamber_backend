from repositories import BaseRepo
from models import DoctorEpHeader
from schemas import DoctorEpHeaderIn, DoctorEpHeaderUpdate

doctor_ep_header_repo = BaseRepo[DoctorEpHeader, DoctorEpHeaderIn, DoctorEpHeaderUpdate](DoctorEpHeader)
