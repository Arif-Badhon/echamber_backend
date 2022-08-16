from repositories import BaseRepo
from models import EpHistory
from schemas import HistoryIn, HistoryUpdate

ep_history_repo = BaseRepo[EpHistory, HistoryIn, HistoryUpdate](EpHistory)
