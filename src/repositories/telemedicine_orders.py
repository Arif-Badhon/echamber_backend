from models.models import HealthPlanList
from repositories import BaseRepo
from schemas import TelemedicineIn, TelemedicineInWithService, TelemedicineUpdate
from models import TeleMedicineOrder
from sqlalchemy.orm import Session
from sqlalchemy import desc


class TelemedicineRepo(BaseRepo[TeleMedicineOrder, TelemedicineInWithService, TelemedicineUpdate]):
    def telemedicine_with_plan(self, db: Session, skip: str, limit: str):
        query = db.query(TeleMedicineOrder, HealthPlanList).join(
        HealthPlanList, TeleMedicineOrder.health_plan_id == HealthPlanList.id).order_by(
            desc(self.model.created_at)).offset(skip).limit(limit).all()
        
        query_all = db.query(TeleMedicineOrder, HealthPlanList).join(
        HealthPlanList, TeleMedicineOrder.health_plan_id == HealthPlanList.id).all()
        
        results = len(query_all)
        return [{"results": results}, query]
                
telemedicine_repo = TelemedicineRepo(TeleMedicineOrder)
