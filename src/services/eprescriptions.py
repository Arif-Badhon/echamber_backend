from schemas.eprescriptions import EpIn, EpUpdate
from services import BaseService
from repositories import ep_repo
from models import EPrescription
from sqlalchemy.orm import Session


class EPrescriptionService(BaseService[EPrescription, EpIn, EpUpdate]):

    def submit(self, data_in: EpIn):
        print(data_in)
        return data_in


ep_service = EPrescriptionService(EPrescription, ep_repo)
