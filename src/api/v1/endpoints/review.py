from typing import List, Union
from fastapi import APIRouter, Depends
from exceptions.service_result import handle_result
from schemas import ReviewIn, ReviewOut, ResultInt, ReviewWithUser
from db import get_db
from api.v1.auth_dependcies import logged_in, logged_in_admin_moderator
from sqlalchemy.orm import Session
from services import review_service

router = APIRouter()


@router.get('/', response_model=List[Union[ResultInt, List[ReviewOut]]])
def all_review(service_name: str, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = review_service.get_by_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, service_name=service_name)
    return handle_result(data)


@router.post('/', response_model=ReviewOut)
def post(data_in: ReviewIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    rev = review_service.create(db=db, data_in=ReviewWithUser(user_id=current_user.id, **data_in.dict()))
    return handle_result(rev)


@router.delete('/{id}')
def delete(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    data = review_service.delete_review(db=db, id=id, user_id=current_user.id)
    return handle_result(data)


@router.patch('/visibility/{id}', response_model=ReviewOut)
def visibility(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = review_service.visibility(db=db, id=id)
    return handle_result(data)


@router.get('/{service_name}/{service_id}', response_model=List[Union[ResultInt, List[ReviewOut]]])
def comment_list(service_name: str, service_id: int, skip: int = 0, limit: int = 10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    data = review_service.get_by_two_key(db=db, skip=skip, limit=limit, descending=True, count_results=True, service_name=service_name, service_id=service_id)
    return handle_result(data)
