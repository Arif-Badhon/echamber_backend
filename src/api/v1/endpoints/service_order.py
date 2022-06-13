from fastapi import APIRouter, Depends
from typing import List, Union
from db import get_db
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, MedicineOrderIn, AdminPanelActivityOut, ServiceOrderOut
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_admin_moderator, logged_in_employee
from services import service_order_service

router = APIRouter()

@router.get('/', response_model=List[ServiceOrderOut], description='Access: employee')
def all_service_order(skip:int = 0, limit:int=15 ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = service_order_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True)
    return handle_result(data)


@router.post('/medicine', response_model=AdminPanelActivityOut, description='Access: admin and moderator')
def medicine_order(data_in:List[Union[ServiceOrderIn, List[MedicineOrderIn]]], db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    medicine_order = service_order_service.medicine_order(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(medicine_order)


@router.get('/medicine/{service_id}')
def medicine_list_by_service(service_id: int ,db: Session = Depends(get_db)):
    print(service_id)
    return 