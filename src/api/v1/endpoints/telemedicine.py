from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, TelemedicineIn, TelemedicineUpdate, TelemedicineOut, AdminPanelActivityOut, ResultInt
from typing import List, Union
from sqlalchemy.orm import Session
from db import get_db
from api.v1.auth_dependcies import logged_in, logged_in_moderator
from services import telemedicine_service


router = APIRouter()

# List[Union[ResultInt, List[AdminPanelActivityOut]]]


@router.get('/', response_model=List[Union[ResultInt, List[TelemedicineOut]]])
def all_telemedicine(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    all = telemedicine_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(all)


@router.get('/single/{id}', response_model=TelemedicineOut)
def single_telemedicine(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    data = telemedicine_service.get_one(db=db, id=id)
    return handle_result(data)


@router.patch('/single/update/{id}', response_model=TelemedicineOut)
def update(id: int, data_update: TelemedicineUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    edit = telemedicine_service.update(db=db, id=id, data_update=data_update)
    return handle_result(edit)
