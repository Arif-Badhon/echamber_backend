from repositories import BaseRepo
from schemas import EpMedicineWithEp, EpMedicineUpdate
from models import EpMedicine

ep_medicines_repo = BaseRepo[EpMedicine, EpMedicineWithEp, EpMedicineUpdate](EpMedicine)
