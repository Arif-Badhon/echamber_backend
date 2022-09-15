from repositories import BaseRepo
from models import EpOnExamination
from schemas import EpOnExaminationIn, EpOnExaminationUpdate


ep_on_examination_repo = BaseRepo[EpOnExamination, EpOnExaminationIn, EpOnExaminationUpdate](EpOnExamination)
