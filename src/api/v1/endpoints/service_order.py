from typing import List, Union
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, ServiceOrderOut, ResultInt, ServiceOrderUpdate
from api.v1.auth_dependcies import get_db, logged_in_employee
from services import service_order_service



router = APIRouter()

@router.get('/', response_model=List[Union[ResultInt, List[ServiceOrderOut]]])
def all_service_order():
    return


@router.post('/', response_model=ServiceOrderOut)
def service_order_in(data_in:ServiceOrderIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    service = service_order_service.create(db=db, data_in=data_in)
    return handle_result(service)

@router.patch('/{id}', response_model=ServiceOrderOut)
def service_order_edit(data_update: ServiceOrderUpdate, id:int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    service = service_order_service.update(db=db,data_update=data_update, id=id)
    return handle_result(service)