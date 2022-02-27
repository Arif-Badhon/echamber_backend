from datetime import timedelta
from db import settings
from exceptions.app_exceptions import AppException
from exceptions.service_result import ServiceResult
from schemas import Token
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import UserCreate, UserOut, UserLogin
from services import users_service
from fastapi.security import OAuth2PasswordRequestForm, HTTPBasic, HTTPBasicCredentials

from utils.password_utils import create_access_token

router = APIRouter()


security = HTTPBasic()


@router.post('/signup', response_model=UserOut)
def signup(data_in: UserCreate, db: Session = Depends(get_db)):
    user = users_service.signup(db, data_in)
    return handle_result(user)


@router.post('/login')
def login(db: Session = Depends(get_db), data_in: OAuth2PasswordRequestForm = Depends()):
    user = users_service.is_auth(
        db, identifier=data_in.username, password=data_in.password)

    if not user:
        return handle_result(
            ServiceResult(AppException.BadRequest(
                "Incorrect username or password"))
        )
    elif not user.is_active:
        return handle_result(ServiceResult(AppException.BadRequest("User is inactive")))

    access_token_expires = timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(user.email, access_token_expires)

    return {"access_token": access_token, "token_type": "bearer"}

# data_in: UserLogin,
