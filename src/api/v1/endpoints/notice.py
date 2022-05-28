from typing import List
from fastapi import APIRouter, Depends, UploadFile, File
from db import get_db
from api.v1.auth_dependcies import logged_in, logged_in_admin, logged_in_admin_moderator
from sqlalchemy.orm import Session
from exceptions.service_result import handle_result
from schemas import NoticeBase, NoticeOut, ImageLogIn, ImageLogOut
from services import notice_service
from utils import UploadFileUtils
from services import image_log_service

router = APIRouter()

# @router.get('/', response_model=List[NoticeOut])
# def all_notice(skip: int, limit: int, db: Session, current_user: Session = Depends(logged_in_admin_moderator)):
#     return


@router.post('/', response_model=NoticeOut)
def create_notice( data_in:NoticeBase ,db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    notice = notice_service.create_with_user(db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(notice)



@router.post('/notice-cover', response_model= ImageLogOut, description='<h2>Alert: </h2> <b>image should be < 300 kb</b>')
async def upload_image(file: UploadFile = File(...), db:Session = Depends(get_db), current_user:Session = Depends(logged_in)):

    up_img = UploadFileUtils(file=file)
    
    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix='notice', path='./assets/img/notice', accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=current_user.id, service_name='notice', image_string=new_image_name))
    

    return handle_result(image_in_db)