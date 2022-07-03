from exceptions.service_result import handle_result
from services import BaseService
from repositories import telemedicine_repo, admin_panel_activity_repo
from models import TeleMedicineOrder
from schemas import TelemedicineIn, TelemedicineInWithService, TelemedicineUpdate, ServiceOrderIn, AdminPanelActivityIn
from sqlalchemy.orm import Session
from typing import List, Union
from .service_order import service_order_service
from exceptions import ServiceResult, AppException
from fastapi import status


class TelemedicineService(BaseService[TeleMedicineOrder, TelemedicineInWithService, TelemedicineUpdate]):

    def create_with_service(self, db: Session, user_id, data_in: List[Union[ServiceOrderIn, TelemedicineIn]]):

        service = service_order_service.create_with_flush(
            db=db, data_in=ServiceOrderIn(data_in[0]))

        telemed = telemedicine_service.create_with_flush(db=db, data_in=TelemedicineInWithService(
            service_id=handle_result(service).id, **data_in[1].dict()))

        # activitylog
        created_by_employee_data = AdminPanelActivityIn(
            user_id=user_id,
            service_name="telemedicine_order",
            service_recived_id=handle_result(telemed).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(
            db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Telemedicine order."))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


telemedicine_service = TelemedicineService(
    TeleMedicineOrder, telemedicine_repo)
