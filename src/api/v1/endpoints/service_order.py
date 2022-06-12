from fastapi import APIRouter, Depends
from typing import List, Union
from db import get_db
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, MedicineOrderIn, AdminPanelActivityOut, ServiceOrderOut
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_admin_moderator
from services import service_order_service

router = APIRouter()

@router.get('/', response_model=List[ServiceOrderOut])
def all_service_order(skip:int = 0, limit:int=15 ,db: Session = Depends(get_db)):
    data = service_order_service.get_with_pagination(db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.post('/medicine', response_model=AdminPanelActivityOut)
def medicine_order(data_in:List[Union[ServiceOrderIn, List[MedicineOrderIn]]], db: Session = Depends(get_db)):
    medicine_order = service_order_service.medicine_order(db=db, data_in=data_in, user_id=1)
    return handle_result(medicine_order)