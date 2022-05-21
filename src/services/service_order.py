from sqlalchemy.orm import Session
from services import BaseService
from repositories import service_order_repo, admin_panel_activity_repo
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate, AdminPanelActivityIn
from services import ServiceResult, AppException
from fastapi import status

class ServiceOrderService(BaseService[ServiceOrder,ServiceOrderIn, ServiceOrderUpdate]):

    def service_order_all(self, db: Session, skip: int, limit: int):
        service = service_order_repo.all_service_order_search(db=db, skip=skip, limit=limit)

        if not service:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        return ServiceResult(service, status_code=status.HTTP_200_OK)        
    
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


    def update_by_employee(self, db: Session, data_update: ServiceOrderUpdate, id: int,  employee_id: int):
        service_order_update = service_order_repo.update(db=db, data_update=data_update, id=id)

        if not service_order_update:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        else:
            updated_attr = ""
            
            for i in data_update:
                if i[1] is not None :
                    if(len(updated_attr) > 0):
                        updated_attr = updated_attr+", "+i[0]
                    else:
                        updated_attr = updated_attr+i[0]

            activity = AdminPanelActivityIn(
                user_id = employee_id,
                service_name ='service_order_update',
                service_recived_id = service_order_update.patient_id,
                remark = f"updated: {updated_attr}"
            )   

            activity_log = admin_panel_activity_repo.create(db=db, data_in=activity) 

            if not activity_log:
                return ServiceResult(AppException.ServerError("Something went wrong!"))
            return ServiceResult(activity_log, status_code=status.HTTP_200_OK)
        
    

service_order_service = ServiceOrderService(ServiceOrder, service_order_repo)