from typing import List, Union
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions.service_result import handle_result
from schemas.doctor_specialities import DoctorSpecialityOut
from services import doctors_search_service
from schemas import DoctorSearchOut, DoctorSearchIn, UserOut, DoctorSearchOut, DoctorUserWithSpecialities


router = APIRouter()

# DoctorSearch schema inherit other shcemas

# response_model=List[DoctorSearchOut]


@router.get('/', response_model=List[DoctorUserWithSpecialities])
def search(search: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    data = doctors_search_service.doctor_search(db=db, skip=skip, limit=limit, search=search)
    return data
