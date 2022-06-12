from typing import List, Union
from fastapi import status
from exceptions import handle_result, ServiceResult, AppException
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate, MedicineOrderIn, MedicineOrderInWithService, AdminPanelActivityIn
from repositories import service_order_repo, medicine_order_repo, admin_panel_activity_repo
from services import BaseService
from .medicine_order import medicine_order_service
from sqlalchemy.orm import Session

class ServiceOrderService(BaseService[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):

    # order keyword
    #--------------
    # medicine order = medicine_order
    
    ###############################
    #                             #
    #    Medicine Service Order   #
    #                             #
    ###############################
    
    def medicine_order(self, db: Session, data_in: List[Union[ServiceOrderIn, List[MedicineOrderIn]]], user_id: int):
    
        #service
        data_obj = data_in[0].dict(exclude={'service_name'})
        data_obj.update({"service_name":"medicine_order"})
        service_flash = self.create_with_flush(db=db, data_in=ServiceOrderIn(**data_obj))
        # print(service_flash.id)
    
        #medicine
        medicine_list_len = len(data_in[1])
        i = 0
        while i < medicine_list_len:
            medicine_order_service.create_with_flush(db=db, data_in=MedicineOrderInWithService(service_order_id=handle_result(service_flash).id, **data_in[1][i].dict()))
            i += 1

        #activitylog
        created_by_employee_data = AdminPanelActivityIn(
                user_id=user_id,
                service_name="medicine_order",
                service_recived_id=handle_result(service_flash).id,
                remark=""
            )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Medicine order."))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


service_order_service = ServiceOrderService(ServiceOrder, service_order_repo)