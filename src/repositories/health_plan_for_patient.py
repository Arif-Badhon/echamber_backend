from repositories import BaseRepo
from models import HealthPlanForPatient
from schemas import HealthPlanForPatientIn, HealthPlanForPatientUpdate

health_plan_for_patient_repo = BaseRepo[HealthPlanForPatient, HealthPlanForPatientIn, HealthPlanForPatientUpdate](HealthPlanForPatient)