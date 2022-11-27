from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in
from db import get_db
from exceptions import handle_result
from schemas import UserDetailOut, UserDetailUpdate
from services import user_details_service
from typing import List

router = APIRouter()


@router.get('/', response_model=UserDetailOut)
def get_detals(db: Session = Depends(get_db), current_user=Depends(logged_in)):
    user_detais = user_details_service.get_by_user_id(db, id=current_user.id)
    return handle_result(user_detais)


@router.patch('/', response_model=UserDetailOut)
def update_details(data_update: UserDetailUpdate, db: Session = Depends(get_db), current_user=Depends(logged_in)):
    update_user_detail = user_details_service.update_by_user_id(
        db, user_id=current_user.id, data_update=data_update)
    return handle_result(update_user_detail)
