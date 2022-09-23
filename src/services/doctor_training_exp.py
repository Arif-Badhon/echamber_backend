from models import DoctorTrainingExp
from schemas import DoctorTrainingExpIn, DoctorTrainingExpUpdate
from repositories import doctor_training_exp_repo
from services import BaseService

doctor_training_exp_services = BaseService[DoctorTrainingExp, DoctorTrainingExpIn, DoctorTrainingExpUpdate](DoctorTrainingExp, doctor_training_exp_repo)