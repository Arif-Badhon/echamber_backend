from typing import List
from fastapi import APIRouter, Depends
from db import get_db
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_admin_moderator
from exceptions.service_result import handle_result
from schemas import MedivaDeviceCatagoryOut, MedivaDeviceCatagoryIn, MedivaDeviceCatagoryUpdate
from services import mediva_device_catagory_service


router = APIRouter()


@router.get('/', response_model=List[MedivaDeviceCatagoryOut])
def all_catagory(db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = mediva_device_catagory_service.get(db=db)
    return handle_result(data)


@router.post('/', response_model=MedivaDeviceCatagoryOut)
def create(data_in: MedivaDeviceCatagoryIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = mediva_device_catagory_service.create(db=db, data_in=data_in)
    return handle_result(data)


@router.get('/{id}', response_model=MedivaDeviceCatagoryOut)
def single(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = mediva_device_catagory_service.get_one(db=db, id=id)
    return handle_result(data)


@router.patch('/{id}', response_model=MedivaDeviceCatagoryOut)
def edit(id: int, data_update: MedivaDeviceCatagoryUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    data = mediva_device_catagory_service.update(db=db, id=id, data_update=data_update)
    return handle_result(data)


@router.delete('/{id}')
def remove(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    remove = mediva_device_catagory_service.delete(db=db, id=id)
    return handle_result(remove)
