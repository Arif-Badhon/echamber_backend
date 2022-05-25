from typing import List
from schemas import Token
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from exceptions import handle_result
from schemas import UserCreate, UserOut, UserOutAuth, UserLogin, NewPasswordIn, UserUpdate, Token, ImageLogOut, ImageLogIn
from services import users_service, image_log_service
from fastapi.security import HTTPBasic
from models import User
from api.v1.auth_dependcies import logged_in
from utils import UploadFileUtils

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


@router.get('/auth', response_model=UserOutAuth)
def auth(current_user: User = Depends(logged_in)):
    return current_user


@router.put('/password/new', response_model=Token)
def new_password(new_password: NewPasswordIn,  db: Session = Depends(get_db), current_user: User = Depends(logged_in)):
    new = users_service.new_password(
        db, user_id=current_user.id, data_update=new_password)
    return handle_result(new)


@router.put('/user/update', response_model=UserOut)
def user_update(user_update: UserUpdate, db: Session = Depends(get_db), current_user: User = Depends(logged_in)):
    user = users_service.user_update(
        db, id=current_user.id, data_update=user_update)
    return handle_result(user)


@router.get('/user/{id}', response_model=UserOutAuth)
def user_by_id(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    user = users_service.get_one(db=db, id=id)
    return handle_result(user)


@router.get('/user/phone/{number}', response_model=List[UserOutAuth])
def user_by_phone(number: str, skip:int=0, limit:int=10,  db: Session = Depends(get_db), current_user: Session = Depends(logged_in)):
    users = users_service.user_search_by_phone(db=db, phone_in=number, skip=skip, limit=limit)
    return handle_result(users)




@router.get('/profile-pic', response_model= ImageLogOut, description='<h2>Alert: files/(image url)</b>')
def get_profile_pic(db:Session = Depends(get_db), current_user:Session = Depends(logged_in)):
    pp = image_log_service.last_profile_pic(db=db, user_id=current_user.id)
    return handle_result(pp)

@router.post('/profile-pic', response_model= ImageLogOut, description='<h2>Alert: </h2> <b>image should be < 300 kb</b>')
async def upload_image(file: UploadFile = File(...), db:Session = Depends(get_db), current_user:Session = Depends(logged_in)):

    up_img = UploadFileUtils(file=file)
    
    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix='propic', accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=current_user.id, service_name='propic', image_string=new_image_name))
    

    return handle_result(image_in_db)
