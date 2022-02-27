from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.v1.auth_dependcies import get_current_active_user
from db import get_db
from exceptions import handle_result
from models import User
from schemas import DoctorOut
from services import doctors_service

router = APIRouter()


@router.get('/', response_model=List[DoctorOut])
def get(db: Session = Depends(get_db)):
    doctor = doctors_service.get(db)
    return handle_result(doctor)
