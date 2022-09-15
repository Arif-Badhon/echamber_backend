from repositories import BaseRepo
from models import EpAdvices
from schemas import AdviceInWithEp, AdviceUpdate

ep_advices_repo = BaseRepo[EpAdvices, AdviceInWithEp, AdviceUpdate](EpAdvices)
