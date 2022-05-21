from sqlalchemy.orm import Session
from services import BaseService
from repositories import service_order_repo, admin_panel_activity_repo
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate, AdminPanelActivityIn
from services import ServiceResult, AppException
from fastapi import status

class ServiceOrderService(BaseService[ServiceOrder,ServiceOrderIn, ServiceOrderUpdate]):
    
    def created_by_employee(self, db: Session, data_in: ServiceOrderIn, employee_id: int):
        service_order_flush = service_order_repo.create_with_flush(db=db, data_in=data_in)

        activity = AdminPanelActivityIn(
            user_id = employee_id,
            service_name ='service_order_input',
            service_recived_id = service_order_flush.patient_id,
            remark = ""
        )

        activity_log = admin_panel_activity_repo.create(db=db, data_in=activity) 
        
        if not activity_log:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(activity_log, status_code=status.HTTP_201_CREATED)

    def updated_by_employee(self, db: Session, data_update: ServiceOrderUpdate, employee_id: int):
        print(employee_id)
        print(data_update)
        return

service_order_service = ServiceOrderService(ServiceOrder, service_order_repo)