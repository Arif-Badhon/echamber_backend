from models import FollowUp
from repositories import BaseRepo
from schemas import FollowUpInWithServiceId, FollowUpUpdate

follow_up_repo = BaseRepo[FollowUp, FollowUpInWithServiceId, FollowUpUpdate](FollowUp)
