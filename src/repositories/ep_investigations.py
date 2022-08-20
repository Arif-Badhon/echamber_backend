from repositories import BaseRepo
from models import EpInvestigation
from schemas import EpInvestigationWithEp, EpInvestigationUpdate


ep_investigation_repo = BaseRepo[EpInvestigation, EpInvestigationWithEp, EpInvestigationUpdate](EpInvestigation)
