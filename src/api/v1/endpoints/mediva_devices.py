from typing import List, Union
from fastapi import APIRouter, Depends, UploadFile
from sqlalchemy.orm import Session
from db import get_db
from exceptions.service_result import handle_result
from services import mediva_device_service, image_log_service
from schemas import MedivaDeviceOut, ResultInt, MedivaDeviceIn, ImageLogOut, ImageLogIn
from api.v1.auth_dependcies import logged_in_moderator
from fastapi import UploadFile, File
from utils import UploadFileUtils

router = APIRouter()

#  response_model=List[ResultInt, List[MedivaDeviceOut]]


@router.get('/', response_model=List[Union[ResultInt, List[MedivaDeviceOut]]])
def all(skip: int = 0, limit: int = 16, db: Session = Depends(get_db)):
    data = mediva_device_service.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
    return handle_result(data)


@router.post('/', response_model=MedivaDeviceOut)
def append(data_in: MedivaDeviceIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):
    data = mediva_device_service.create(db=db, data_in=data_in)
    handle_result(data)


@router.post('/img', response_model=ImageLogOut, description='<h2>Alert: </h2> <b>image should be < 300 kb</b>')
async def upload_image(file: UploadFile = File(...), db: Session = Depends(get_db), current_user: Session = Depends(logged_in_moderator)):

    up_img = UploadFileUtils(file=file)

    # prefix is the short service name
    new_image_name = up_img.upload_image(prefix='mediva_devices', path='./assets/img/mediva_devices', accepted_extensions=['jpg', 'jpeg', 'png'])

    # save in db
    image_in_db = image_log_service.create(db=db, data_in=ImageLogIn(user_id=current_user.id, service_name='notice', image_string=new_image_name))

    return handle_result(image_in_db)
