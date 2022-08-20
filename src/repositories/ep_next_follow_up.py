from repositories import BaseRepo
from schemas import EpNextFollowUpWithEp, EpNextFollowUpUpdate
from models import EpNextFollowUp

ep_next_follow_up_repo = BaseRepo[EpNextFollowUp, EpNextFollowUpWithEp, EpNextFollowUpUpdate](EpNextFollowUp)
