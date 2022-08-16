from typing import List, Union
from fastapi import APIRouter, Depends
from db.db_session import get_db
from exceptions.service_result import handle_result
from schemas.follow_up import FollowUpIn, FollowUpUpdate
from services import follow_up_service
from schemas import FollowUpOut, ResultInt, AdminPanelActivityOut
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_employee, logged_in_crm


router = APIRouter()


@router.get('/', response_model=List[Union[ResultInt, List[FollowUpOut]]])
def all_followup(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = follow_up_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(data)


@router.post('/', response_model=AdminPanelActivityOut, description='status: pending, done')
def create_follow_up(data_in: FollowUpIn, service_id: int, current_user: Session = Depends(logged_in_crm), db: Session = Depends(get_db)):
    create_follow_up = follow_up_service.create_with_service(db=db, data_in=data_in, service_id=service_id, user_id=current_user.id)
    return handle_result(create_follow_up)


@router.patch('/{id}', response_model=FollowUpOut)
def update_followup(id: int, data_update: FollowUpUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_crm)):
    up = follow_up_service.update(db=db, data_update=data_update, id=id)
    return handle_result(up)


@router.get('/service/{id}', response_model=List[Union[ResultInt, List[FollowUpOut]]])
def search_by_service(id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_crm)):
    service_by = follow_up_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, service_id=id)
    return handle_result(service_by)


@router.get('/date/{date}', response_model=List[Union[ResultInt, List[FollowUpOut]]])
def search_by_date(date: str, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_crm)):
    date_by = follow_up_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=True, followup_date=date)
    return handle_result(date_by)


@router.get('/status/{follow_up_status}', response_model=List[Union[ResultInt, List[FollowUpOut]]])
def search_by_status(follow_up_status: str, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_crm)):
    data = follow_up_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, status=follow_up_status)
    return handle_result(data)
