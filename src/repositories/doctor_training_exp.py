from repositories import BaseRepo
from models import DoctorTrainingExp
from schemas import DoctorTrainingExpIn, DoctorTrainingExpUpdate

doctor_training_exp_repo = BaseRepo[DoctorTrainingExp, DoctorTrainingExpIn, DoctorTrainingExpUpdate](DoctorTrainingExp)
