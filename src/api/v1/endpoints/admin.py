from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreateWitoutRole
from sqlalchemy.orm import Session
from services import admin_service
from api.v1.auth_dependcies import logged_in_admin, logged_in_moderator


router = APIRouter()


@router.get('/auth', response_model=UserOut)
def auth(admin: Session = Depends(logged_in_admin)):
    return admin


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreateWitoutRole, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)


@router.get('/auth/moderator', response_model=UserOut)
def moderator_auth(moderator: Session = Depends(logged_in_moderator)):
    return moderator


@router.post('/create/moderator', response_model=UserOut)
def moderator_create(data_in: UserCreateWitoutRole, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin)):
    moderator = admin_service.signup_moderator(db, data_in=data_in)
    return handle_result(moderator)
