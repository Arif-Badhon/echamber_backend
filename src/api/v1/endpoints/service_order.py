from fastapi import APIRouter, Depends
from typing import List, Union
from db import get_db
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, MedicineOrderIn, AdminPanelActivityOut, ServiceOrderOut, ResultInt, MedicineOrderOut, TelemedicineServiceIn
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_admin_crm, logged_in_admin_moderator, logged_in_employee
from schemas.medicine_order import MedicineOrderUpdate
from schemas.service_order import ServiceOrderUpdate
from schemas.telemedicine_orders import TelemedicineIn
from services import service_order_service, medicine_order_service, telemedicine_service

router = APIRouter()


@router.get('/', response_model=List[Union[ResultInt, List[ServiceOrderOut]]], description='Access: employee')
def all_service_order(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = service_order_service.all_service_order(
        db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.get('/{id}', response_model=ServiceOrderOut)
def single_service(id: int, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    single = service_order_service.get_one(db=db, id=id)
    return handle_result(single)


@router.get('/patient/{id}', response_model=List[Union[ResultInt, List[ServiceOrderOut]]])
def patient_services(id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    pt = service_order_service.get_by_key(
        db=db, skip=skip, limit=limit, descending=True, count_results=True, patient_id=id)
    return handle_result(pt)


@router.patch('/{id}', response_model=ServiceOrderOut)
def update_service(id: int, data_update: ServiceOrderUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_crm)):
    up = service_order_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)


@router.post('/telemedicine', response_model=AdminPanelActivityOut)
def telemedicine_order(data_in: TelemedicineServiceIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    telemed = telemedicine_service.create_with_service(db=db, user_id=current_user.id, data_in=data_in)
    return handle_result(telemed)


@router.post('/medicine', response_model=AdminPanelActivityOut, description='Access: admin and moderator')
def medicine_order(data_in: List[Union[ServiceOrderIn, List[MedicineOrderIn]]], db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_moderator)):
    medicine_order = service_order_service.medicine_order(
        db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(medicine_order)


@router.get('/medicine/{service_id}', response_model=List[Union[ResultInt, List[MedicineOrderOut]]])
def medicine_list_by_service(service_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = medicine_order_service.get_by_key(
        db=db, skip=skip, limit=limit, descending=False, count_results=True, service_order_id=service_id)
    return handle_result(data)


@router.patch('/medicine/update/{id}', response_model=MedicineOrderOut)
def update_medicine(id: int, data_update: MedicineOrderUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_admin_crm)):
    up = medicine_order_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)
