from fastapi import APIRouter, Depends
from schemas import PatientIndicatorOut
from typing import List
from services import patient_indicators_service
from sqlalchemy.orm import Session
from db import get_db
from api.v1.auth_dependcies import logged_in_doctor
from exceptions import handle_result

router = APIRouter()


@router.get('/patient/indicator/{key}/{user_id}', response_model=List[PatientIndicatorOut])
def patient_indicator_get(key: str, user_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    indicators = patient_indicators_service.get_by_key(db=db, key=key, user_id=user_id, skip=skip, limit=limit)
    return handle_result(indicators)
