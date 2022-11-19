from datetime import date
from exceptions.service_result import handle_result
from repositories import health_plan_for_patient, health_plan_for_patient_repo, admin_panel_activity_repo
from schemas.health_plan import HealthPlanForPatientWithoutHealthPlanId
from services import BaseService
from models import HealthPlanForPatient
from schemas import HealthPlanForPatientIn, HealthPlanForPatientUpdate, AdminPanelActivityIn, HealthPlanForPatientWithService, ServiceOrderIn
from .health_plan_list import healtth_plan_list_service
from .service_order import service_order_service
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class HealthPlanForPatient(BaseService[HealthPlanForPatient, HealthPlanForPatientIn, HealthPlanForPatientUpdate]):

    def subscribe_with_service(self, db: Session, voucher_code: str, employee_id: int, data_in: HealthPlanForPatientWithService):
        service = service_order_service.create_with_flush(db=db, data_in=ServiceOrderIn(**data_in.dict()['service']))

        # healthplan id
        by_voucher = healtth_plan_list_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, voucher_code=voucher_code)
        health_plan_id = handle_result(by_voucher)[0].id

        if not health_plan_id:
            return ServiceResult(AppException.ServerError("Wrong Voucher Code."))

        # healthplan subscribe
        healthplan_for_patient = health_plan_for_patient_service.create_with_flush(db=db, data_in=HealthPlanForPatientIn(
            service_order_id=handle_result(service).id, health_plan_id=health_plan_id, **data_in.dict()['health_plan_subscribe']))

        if not health_plan_for_patient:
            return ServiceResult(AppException.ServerError("Problem with subscribe"))

        # activity log
        created_by_employee_data = AdminPanelActivityIn(
            user_id=employee_id,
            service_name="health_plan_subscribe",
            service_recived_id=handle_result(healthplan_for_patient).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Health Plan Activity"))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


health_plan_for_patient_service = HealthPlanForPatient(HealthPlanForPatient, health_plan_for_patient_repo)
