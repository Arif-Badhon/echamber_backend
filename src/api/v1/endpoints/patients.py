from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from exceptions import handle_result
from schemas import PatientOut
from db import get_db
from services import patients_service

router = APIRouter()


@router.get('/', response_model=List[PatientOut])
def get(db: Session = Depends(get_db)):
    patients = patients_service.get(db)
    return handle_result(patients)
