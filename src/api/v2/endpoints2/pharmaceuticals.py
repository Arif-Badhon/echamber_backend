from typing import List
from fastapi import APIRouter, Depends
from api.v1.endpoints.doctor_chambers import get
from exceptions.service_result import handle_result
from schemas import PharmaceuticalOut, PharmaceuticalUserWithPhr
from db import get_db
from sqlalchemy.orm import Session
from services import pharmaceutical_service
from api.v1.auth_dependcies import logged_in_admin

router = APIRouter()

@router.get("/", response_model=List[PharmaceuticalOut])
def read(db: Session = Depends(get_db)):
    search = pharmaceutical_service.get(db=db)
    return handle_result(search)

@router.post("/")
def phr_with_user(data_in: PharmaceuticalUserWithPhr, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    user = pharmaceutical_service.register_pharmaceuticals(db=db, data_in=data_in)
    return handle_result(user)
