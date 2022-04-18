from fastapi import APIRouter, Depends
from db import get_db
from exceptions.service_result import handle_result
from schemas import UserOut, UserCreate
from sqlalchemy.orm import Session
from services import admin_service
from api.v1.auth_dependcies import logged_in_admin


router = APIRouter()


@router.get('/auth', response_model=UserOut)
def auth(admin: Session = Depends(logged_in_admin)):
    return admin


@router.post('/', response_model=UserOut)
def signup(data_in: UserCreate, db: Session = Depends(get_db)):
    admn = admin_service.signup_admin(db, data_in=data_in)
    return handle_result(admn)
