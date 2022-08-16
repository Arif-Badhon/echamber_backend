from repositories import BaseRepo
from models import EpDoctorRefer
from schemas import EpDoctorReferIn, EpDoctorReferUpdate

ep_refer_repo = BaseRepo[EpDoctorRefer, EpDoctorReferIn, EpDoctorReferUpdate](EpDoctorRefer)
