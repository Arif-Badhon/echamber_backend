from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from services import healtth_plan_list_service
from schemas import HealthPlanListIn, HealthPlanListOut
from db import get_db
from api.v1.auth_dependcies import logged_in_admin

router = APIRouter()


@router.get('/',  response_model=List[HealthPlanListOut])
def get(db:Session = Depends(get_db)):
    health_plan_list = healtth_plan_list_service.get(db=db)
    return handle_result(health_plan_list)


@router.post('/', response_model=HealthPlanListOut)
def post(data_in: HealthPlanListIn, db: Session = Depends(get_db), current_user:Session = Depends(logged_in_admin)):
    health_plan = healtth_plan_list_service.create(db=db, data_in=data_in)
    return handle_result(health_plan)
