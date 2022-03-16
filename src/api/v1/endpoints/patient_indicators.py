from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import PatientIndicatorOut, PatientIndicatorBase
from sqlalchemy.orm import Session
from db import get_db
from services import patient_indicators_service
from api.v1.auth_dependcies import logged_in_patient
from typing import List

router = APIRouter()


@router.post('/', response_model=PatientIndicatorOut)
def create(data_in: PatientIndicatorBase, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    patient_indicator = patient_indicators_service.create_by_user_id(
        db, user_id=current_user.id, data_in=data_in)
    return handle_result(patient_indicator)


@router.get('/{key}', response_model=List[PatientIndicatorOut])
def get_by_key(key: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    indicators = patient_indicators_service.get_by_key(
        db, key, user_id=current_user.id)
    return handle_result(indicators)


@router.get('/last/{key}', response_model=PatientIndicatorOut)
def get_last_item(key: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_patient)):
    last = patient_indicators_service.get_last_item(
        db, key, user_id=current_user.id)
    return handle_result(last)
