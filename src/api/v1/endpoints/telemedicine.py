from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, TelemedicineIn, AdminPanelActivityOut
from typing import List, Union
from sqlalchemy.orm import Session
from db import get_db
from api.v1.auth_dependcies import logged_in_admin_moderator
from services import telemedicine_service


router = APIRouter()


@router.get('/')
def all_telemedicine():
    return {'msg': 'Telemedicine'}


@router.post('/', response_model=AdminPanelActivityOut)
def create(data_in: List[Union[ServiceOrderIn, TelemedicineIn]], db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = telemedicine_service.create_with_service(db=db, user_id=current_user.id, data_in=data_in)
    return handle_result(data)
