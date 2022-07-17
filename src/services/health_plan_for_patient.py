from datetime import date
from exceptions.service_result import handle_result
from repositories import health_plan_for_patient_repo, admin_panel_activity_repo
from schemas.health_plan import HealthPlanForPatientWithoutHealthPlanId
from services import BaseService
from models import HealthPlanForPatient
from schemas import HealthPlanForPatientIn, HealthPlanForPatientUpdate, AdminPanelActivityIn, HealthPlanForPatientWithService
from .health_plan_list import healtth_plan_list_service
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class HealthPlanForPatient(BaseService[HealthPlanForPatient, HealthPlanForPatientIn, HealthPlanForPatientUpdate]):

    def subscribe_plan(self, db: Session, data_in: HealthPlanForPatientWithoutHealthPlanId, voucher_code: str, employee_id: int):
        by_voucher = healtth_plan_list_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, voucher_code=voucher_code)
        health_plan_id = handle_result(by_voucher)[0].id

        if not health_plan_id:
            return ServiceResult(AppException.ServerError("Wrong Voucher Code."))

        # total_patient_check

        expire_status = handle_result(by_voucher)[0].expire_status
        if expire_status is True:
            return ServiceResult(AppException.ServerError("Plan Expire date is over."))
        # expire detail check

        # check all exception are pending

        hp = health_plan_for_patient_service.create_with_flush(db=db, data_in=HealthPlanForPatientIn(health_plan_id=health_plan_id, **data_in.dict()))

        if not hp:
            return ServiceResult(AppException.ServerError(
                "Problem with Health plan subcribe."))
        else:
            created_by_employee_data = AdminPanelActivityIn(
                user_id=employee_id,
                service_name="health_plan_subscribe",
                service_recived_id=handle_result(hp).id,
                remark=""
            )

            created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)

            if not created_by_employee:
                return ServiceResult(AppException.ServerError("Problem with Health Plan Activity"))
            else:
                return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)

    def subscribe_with_service(self, db: Session, voucher_code: str, employee_in: int, data_in: HealthPlanForPatientWithService):
        return


health_plan_for_patient_service = HealthPlanForPatient(HealthPlanForPatient, health_plan_for_patient_repo)
