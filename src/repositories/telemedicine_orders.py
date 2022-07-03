from repositories import BaseRepo
from schemas import TelemedicineIn, TelemedicineInWithService, TelemedicineUpdate
from models import TeleMedicineOrder

telemedicine_repo = BaseRepo[TeleMedicineOrder,
                             TelemedicineInWithService, TelemedicineUpdate](TeleMedicineOrder)
