from repositories import BaseRepo
from models import EpCoMorbidity
from schemas import EpCoMorbidityWithEp, EpCoMorbidityUpdate

ep_co_morbities_repo = BaseRepo[EpCoMorbidity, EpCoMorbidityWithEp, EpCoMorbidityUpdate](EpCoMorbidity)
