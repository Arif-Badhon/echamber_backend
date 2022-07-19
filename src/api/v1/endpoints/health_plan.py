from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from schemas.health_plan import HealthPlanForPatientWithoutHealthPlanId
from services import healtth_plan_list_service, health_plan_for_patient_service
from schemas import HealthPlanListIn, HealthPlanListOut, HealthPlanForPatientIn, HealthPlanForPatientOut, AdminPanelActivityOut, HealthPlanListUpdate
from db import get_db
from api.v1.auth_dependcies import logged_in, logged_in_admin, logged_in_employee

router = APIRouter()


@router.get('/',  response_model=List[HealthPlanListOut])
def get(db: Session = Depends(get_db)):
    health_plan_list = healtth_plan_list_service.get(db=db)
    return handle_result(health_plan_list)


@router.post('/', response_model=HealthPlanListOut)
def post(data_in: HealthPlanListIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    health_plan = healtth_plan_list_service.create(db=db, data_in=data_in)
    return handle_result(health_plan)


@router.get('/{id}', response_model=HealthPlanListOut)
def single_health_plan(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = healtth_plan_list_service.get_one(db=db, id=id)
    return handle_result(data)


@router.patch('/{id}', response_model=HealthPlanListOut)
def edit(id: int, data_update: HealthPlanListUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    up = healtth_plan_list_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)
