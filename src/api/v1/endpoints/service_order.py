from fastapi import APIRouter, Depends
from typing import List, Union
from db import get_db
from exceptions.service_result import handle_result
from schemas import ServiceOrderIn, MedicineOrderIn, HealthPlanForPatientWithService, HealthPlanForPatientOut, AdminPanelActivityOut, ServiceOrderOut, ResultInt, MedicineOrderOut, TelemedicineServiceIn, TelemedicineOut, ServiceOrderoutWithUser
from sqlalchemy.orm import Session
from api.v1.auth_dependcies import logged_in_employee
from schemas.medicine_order import MedicineOrderUpdate
from schemas.service_order import ServiceOrderUpdate
from schemas.telemedicine_orders import TelemedicineIn
from services import service_order_service, medicine_order_service, telemedicine_service, health_plan_for_patient_service

router = APIRouter()


@router.get('/', response_model=List[Union[ResultInt, List[ServiceOrderOut]]], description='Access: employee')
def all_service_order(skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = service_order_service.all_service_order(
        db=db, skip=skip, limit=limit)
    return handle_result(data)


@router.get('/filter', response_model=List[Union[ResultInt, List[ServiceOrderoutWithUser]]], description='Access: employee')
def all_service_filter(
        service_id: int = None, customer_id: int = None, customer_name: str = None, customer_phone: str = None, address: str = None, service_name: str = None, order_date: str = None, order_status: str = None,
        skip: int = 0, limit: int = 15, db: Session = Depends(get_db),
        current_user: Session = Depends(logged_in_employee)):
    data = service_order_service.service_with_patient(db=db, service_id=service_id, customer_id=customer_id, customer_name=customer_name, customer_phone=customer_phone,
                                                      address=address, service_name=service_name, order_date=order_date, order_status=order_status, skip=skip, limit=limit)
    return data


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
def update_service(id: int, data_update: ServiceOrderUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    up = service_order_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)


@router.post('/healthplan/subscribe', response_model=AdminPanelActivityOut)
def health_plan(data_in: HealthPlanForPatientWithService, voucher_code: str, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = health_plan_for_patient_service.subscribe_with_service(db=db, data_in=data_in, voucher_code=voucher_code, employee_id=current_user.id)
    return handle_result(data)


@router.get('/healthplan/subscribe/{service_id}', response_model=List[HealthPlanForPatientOut])
def healthplan_subscription_by_service(service_id: int, skip: int = 0, limit: int = 10, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    hp = health_plan_for_patient_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=False, service_order_id=service_id)
    return handle_result(hp)


@router.post('/telemedicine', response_model=AdminPanelActivityOut)
def telemedicine_order(data_in: TelemedicineServiceIn, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    telemed = telemedicine_service.create_with_service(db=db, user_id=current_user.id, data_in=data_in)
    return handle_result(telemed)


@router.get('/telemedicine/{service_id}', response_model=List[TelemedicineOut])
def telemedicine_by_service_id(service_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 10, current_user: Session = Depends(logged_in_employee)):
    data = telemedicine_service.get_by_key(db=db, skip=skip, limit=limit, descending=False, count_results=False, service_order_id=service_id)
    return handle_result(data)


@router.post('/medicine', response_model=AdminPanelActivityOut, description='Access: admin and moderator')
def medicine_order(data_in: List[Union[ServiceOrderIn, List[MedicineOrderIn]]], db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    medicine_order = service_order_service.medicine_order(
        db=db, data_in=data_in, user_id=current_user.id)
    return handle_result(medicine_order)


@router.get('/medicine/{service_id}', response_model=List[Union[ResultInt, List[MedicineOrderOut]]])
def medicine_list_by_service(service_id: int, skip: int = 0, limit: int = 15, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    data = medicine_order_service.get_by_key(
        db=db, skip=skip, limit=limit, descending=False, count_results=True, service_order_id=service_id)
    return handle_result(data)


@router.patch('/medicine/update/{id}', response_model=MedicineOrderOut)
def update_medicine(id: int, data_update: MedicineOrderUpdate, db: Session = Depends(get_db), current_user: Session = Depends(logged_in_employee)):
    up = medicine_order_service.update(db=db, id=id, data_update=data_update)
    return handle_result(up)
