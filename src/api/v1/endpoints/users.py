from schemas import Token
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import UserCreate, UserOut, UserLogin, Token
from schemas.users import UserUpdate
from services import users_service
from fastapi.security import HTTPBasic
from models import User
from api.v1.auth_dependcies import logged_in


router = APIRouter()


security = HTTPBasic()


@router.post('/signup', response_model=UserOut)
def signup(data_in: UserCreate, db: Session = Depends(get_db)):
    user = users_service.signup(db, data_in)
    return handle_result(user)


@router.post('/login', response_model=Token)
def login(data_in: UserLogin, db: Session = Depends(get_db)):
    user = users_service.login(db, data_in.identifier, data_in.password)
    return handle_result(user)


@router.get('/auth', response_model=UserOut)
def auth(current_user: User = Depends(logged_in)):
    return current_user


@router.put('/user/update', response_model=UserOut)
def user_update(user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(logged_in)):
    user = users_service.update(
        db, id=current_user.id, data_update=user_update)
    return handle_result(user)
