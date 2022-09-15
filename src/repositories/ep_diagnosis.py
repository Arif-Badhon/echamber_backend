from repositories import BaseRepo
from models import EpDiagnosis
from schemas import EpDiagnosisWithEp, EpDiagnosisUpdate

ep_diagnosis_repo = BaseRepo[EpDiagnosis, EpDiagnosisWithEp, EpDiagnosisUpdate](EpDiagnosis)
