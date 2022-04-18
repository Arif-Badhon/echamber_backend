from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions.service_result import handle_result
from services import doctors_search_service
from schemas import DoctorSearchOut


router = APIRouter()

# DoctorSearch schema inherit other shcemas


@router.get('/', response_model=List[DoctorSearchOut])
def search(search_key: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    q = doctors_search_service.doctor_search(
        db=db, search_key=search_key, skip=skip, limit=limit)
    return handle_result(q)
