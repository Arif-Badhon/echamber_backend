from typing import List
from fastapi import APIRouter
from db import get_db
from exceptions.service_result import handle_result
from services import patients_service
from sqlalchemy.orm import Session
from fastapi import Depends
from schemas import EpPatientSearchOut
from api.v1.auth_dependcies import logged_in_doctor

router = APIRouter()


@router.get('/patient-search', response_model=List[EpPatientSearchOut])
def patient_search_by_name(name:str, skip:int=0, limit:int=10, db:Session = Depends(get_db), current_user: Session = Depends(logged_in_doctor)):
    patients = patients_service.search_by_patient_name(db=db, name=name, skip=skip, limit=limit)
    return handle_result(patients)