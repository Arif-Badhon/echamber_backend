from models.models import HealthPlanList
from repositories import BaseRepo
from models import HealthPlanForPatient
from schemas import HealthPlanForPatientIn, HealthPlanForPatientUpdate
from sqlalchemy.orm import Session

class HealthPlanForPatientRepo(BaseRepo[HealthPlanForPatient, HealthPlanForPatientIn, HealthPlanForPatientUpdate]):

    def health_plan_patient(self, db: Session, service_id: int):
        query = db.query(HealthPlanList).filter(
        HealthPlanForPatient.health_plan_id == HealthPlanList.id).filter(
        HealthPlanForPatient.service_order_id == service_id).all()
        
        return query

health_plan_for_patient_repo = HealthPlanForPatientRepo(HealthPlanForPatient)