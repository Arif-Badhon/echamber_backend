from models.models import HealthPlanList, ServiceOrder
from repositories import BaseRepo
from schemas import TelemedicineIn, TelemedicineInWithService, TelemedicineUpdate
from models import TeleMedicineOrder
from sqlalchemy.orm import Session


class TelemedicineRepo(BaseRepo[TeleMedicineOrder, TelemedicineInWithService, TelemedicineUpdate]):

    def telemedicine_with_plan(self, db: Session, service_id: int):
        query = db.query(HealthPlanList).filter(
        TeleMedicineOrder.health_plan_id == HealthPlanList.id).filter(
        TeleMedicineOrder.service_order_id == service_id).all()
        
        return query

                
telemedicine_repo = TelemedicineRepo(TeleMedicineOrder)
