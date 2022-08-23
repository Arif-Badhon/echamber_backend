from typing import List
from fastapi import APIRouter, Depends
from api.v1.endpoints.doctor_chambers import get
from exceptions.service_result import handle_result
from schemas import PharmaceuticalIn, PharmaceuticalOut, AdminPanelActivityOut, PharmaceuticalUserWithPhr
from db import get_db
from sqlalchemy.orm import Session
from services import pharmaceutical_service, pharmaceuticals_user_service

router = APIRouter()

@router.get("/", response_model=List[PharmaceuticalOut])
def read(db: Session = Depends(get_db)):
    acc = pharmaceutical_service.get(db=db)
    return handle_result(acc)

@router.post("/", response_model = AdminPanelActivityOut)
def phr_with_user(data_in: PharmaceuticalUserWithPhr, db: Session = Depends(get_db)):
    user = pharmaceutical_service.create(db=db)
    return handle_result(user)
