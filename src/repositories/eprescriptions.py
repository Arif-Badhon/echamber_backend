from repositories import BaseRepo
from models import EPrescription
from schemas import EpIn, EpUpdate

ep_repo = BaseRepo[EPrescription, EpIn, EpUpdate](EPrescription)
