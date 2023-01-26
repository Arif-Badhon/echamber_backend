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
from .sms import sms_service
from .users import users_service


class HealthPlanForPatient(BaseService[HealthPlanForPatient, HealthPlanForPatientIn, HealthPlanForPatientUpdate]):

    def subscribe_with_service(self, db: Session, voucher_code: str, employee_id: int, data_in: HealthPlanForPatientWithService):
        service = service_order_service.create_with_flush(db=db, data_in=ServiceOrderIn(**data_in.dict()['service']))

        # healthplan by voucher
        by_voucher = healtth_plan_list_service.get_by_key(db=db, skip=0, limit=10, descending=False, count_results=False, voucher_code=voucher_code)
        health_plan = handle_result(by_voucher)
        health_plan_id = health_plan[0].id
        health_plan_name = health_plan[0].name

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

        patient_data = users_service.get_one(db=db, id=data_in.health_plan_subscribe.user_id)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Health Plan Activity"))
        else:
            if voucher_code[0:3] == 'BHP':
                s = sms_service.send_sms(
                    sms_to='88' + handle_result(patient_data).phone,
                    sms='ধন্যবাদ, আমাদের বেসিক হেলথ প্ল্যান টি নেয়ার জন্য। ভবিষ্যতে আপনার স্বাস্থ্য সম্পর্কিত যেকোনো প্রয়োজনে যোগাযোগ করুন 01571-016461, 01322-658481 এই নাম্বারে। \nধন্যবাদান্তে \nHEALTHx ')
            elif voucher_code[0:3] == 'FHP':
                s = sms_service.send_sms(sms_to='88' + handle_result(patient_data).phone, sms='"ফ্যামিলি হেলথ প্ল্যানে" আপনার রেজিস্ট্রেশন টি সঠিকভাবে সম্পন্ন হয়েছে। আপনার প্ল্যান টির মেয়াদ থাকছে ' +
                                         str(data_in.service.order_completion).split(' ')[0] +
                                         ' পর্যন্ত। প্যাকেজ সংক্রান্ত যেকোনো সেবা গ্রহনের জন্য সরাসরি যোগাযোগ করুন 01571-016461, 01322-658481 এই নাম্বারে। \nধন্যবাদান্তে \nHEALTHx')
            elif voucher_code[0:3] == 'MHP':
                s = sms_service.send_sms(sms_to='88' + handle_result(patient_data).phone, sms='"আমার হেলথ প্ল্যানে" আপনার রেজিস্ট্রেশন টি সঠিকভাবে সম্পন্ন হয়েছে। আপনার প্ল্যান টির মেয়াদ থাকছে ' +
                                         str(data_in.service.order_completion).split(' ')[0] +
                                         ' পর্যন্ত। প্যাকেজ সংক্রান্ত যেকোনো সেবা গ্রহনের জন্য সরাসরি যোগাযোগ করুন  01571-016461, 01322-658481 এই নাম্বারে।\nধন্যবাদান্তে \nHEALTHx ')
            else:
                print('')
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)
    

    def health_plan_patient(self, db: Session, service_id: int):
        data = health_plan_for_patient_repo.health_plan_patient(db=db, service_id=service_id)
        
        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(data, status_code=status.HTTP_200_OK)


health_plan_for_patient_service = HealthPlanForPatient(HealthPlanForPatient, health_plan_for_patient_repo)
