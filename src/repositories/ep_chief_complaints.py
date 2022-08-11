from repositories import BaseRepo
from schemas import ChiefComplaintsIn, ChiefComplaintsUpdate
from models import EpChiefComplaints


ep_chief_complaints_repo = BaseRepo[EpChiefComplaints, ChiefComplaintsIn, ChiefComplaintsUpdate](EpChiefComplaints)
