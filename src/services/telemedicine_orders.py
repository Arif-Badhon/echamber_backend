from exceptions.service_result import handle_result
from services import BaseService
from repositories import telemedicine_repo, admin_panel_activity_repo
from models import TeleMedicineOrder
from schemas import TelemedicineIn, TelemedicineInWithService, TelemedicineUpdate, ServiceOrderIn, AdminPanelActivityIn, TelemedicineServiceIn
from sqlalchemy.orm import Session
from typing import List, Union
from .service_order import service_order_service
from exceptions import ServiceResult, AppException
from fastapi import status
from .sms import sms_service
from .users import users_service


class TelemedicineService(BaseService[TeleMedicineOrder, TelemedicineInWithService, TelemedicineUpdate]):

    def create_with_service(self, db: Session, user_id, data_in: TelemedicineServiceIn):

        service = service_order_service.create_with_flush(
            db=db, data_in=ServiceOrderIn(**data_in.dict()['service']))

        telemed = telemedicine_service.create_with_flush(db=db, data_in=TelemedicineInWithService(**data_in.dict()['telemedicine'], service_order_id=handle_result(service).id))

        # activitylog
        created_by_employee_data = AdminPanelActivityIn(
            user_id=user_id,
            service_name="telemedicine_order",
            service_recived_id=handle_result(telemed).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(
            db=db, data_in=created_by_employee_data)

        user = users_service.get_one(db=db, id=data_in.telemedicine.patient_id)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Telemedicine order."))
        else:
            s = sms_service.send_sms(
                sms_to='88' + handle_result(user).phone,
                sms='ধন্যবাদ, আমাদের টেলিমেডিসিন সেবা টি নেয়ার জন্য। আশা করছি  ভবিষ্যতে আপনাদের স্বাস্থ্য সুরক্ষায় এভাবে সহযোগিতা করতে পারবো। \nHEALTHx এর সাথেই থাকুন। \nযেকোনো প্রয়োজনে যোগাযোগ করুন 01571-016461, 01322-658481 এই নাম্বারে। \nধন্যবাদান্তে \nHEALTHx ')
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


telemedicine_service = TelemedicineService(
    TeleMedicineOrder, telemedicine_repo)
