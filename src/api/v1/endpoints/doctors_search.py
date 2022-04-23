from typing import List
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions.service_result import handle_result
from services import doctors_search_service
from schemas import DoctorSearchOut, DoctorSearchIn


router = APIRouter()

# DoctorSearch schema inherit other shcemas

#response_model=List[DoctorSearchOut]
@router.get('/')
def search(name: str, speciality:str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    q = doctors_search_service.doctor_search(
        db=db, name=name, speciality=speciality, skip=skip, limit=limit)
    return handle_result(q)
