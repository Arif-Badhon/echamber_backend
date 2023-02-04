from typing import List, Union
from fastapi import status
from exceptions import handle_result, ServiceResult, AppException
from models import ServiceOrder
from schemas import ServiceOrderIn, ServiceOrderUpdate, MedicineOrderIn, MedicineOrderInWithService, AdminPanelActivityIn
from repositories import service_order_repo, admin_panel_activity_repo, follow_up_repo, users_repo, health_plan_for_patient_repo
from services import BaseService
from .medicine_order import medicine_order_service
from .users import users_service
from sqlalchemy.orm import Session
from .sms import sms_service


class ServiceOrderService(BaseService[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):

    def service_with_patient(
            self, db: Session, service_id: int, customer_id: int, customer_name: str, customer_phone: str, address: str, service_name: str, start_date: str, end_date: str, order_date: str,
            order_status: str, skip: int, limit: int):
        all_service = self.repo.service_with_patient(db=db, service_id=service_id, customer_id=customer_id, customer_name=customer_name, customer_phone=customer_phone, address=address,
        service_name=service_name, start_date=start_date, end_date=end_date, order_date=order_date, order_status=order_status, skip=skip, limit=limit)

        data_with_plan_and_issuer = []
        for i in all_service[1]:
            plans = health_plan_for_patient_repo.health_plan_patient(db=db, service_id=i.ServiceOrder.id)
            issuer = users_repo.get_by_key(db=db, skip=0, limit=2, descending=True, count_results=False, id=i.ServiceOrder.service_issuer_id)

            i.ServiceOrder.plan = plans
            i.ServiceOrder.issuer = issuer
            data_with_plan_and_issuer.append(i)

        data = [{"results": all_service[0]["results"]}, data_with_plan_and_issuer]
        return data

    def patient_with_multiservice(self, db: Session):
        data = self.repo.patient_with_multiservice(db=db)
        if not data:
            return ServiceResult(AppException.ServerError("No data found"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def patient_with_multiservice_range(self, db: Session, start_date: str, end_date: str):
        data = self.repo.patient_with_multiservice_range(db=db, start_date=start_date, end_date=end_date)
        if not data:
            return ServiceResult(AppException.ServerError("No data found"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    # All Service order with detail
    # ------------------------------

    def all_service_order(self, db: Session, skip: int, limit: int):
        data = service_order_repo.get_with_pagination(
            db=db, skip=skip, limit=limit, descending=True, count_results=True)

        final_data = [data[0]]

        new_data = []
        for i in data[1]:

            # Those are only bind here
            # for follow up flag
            fl = follow_up_repo.get_by_key(
                db=db, skip=0, limit=100, descending=False, count_results=True, service_id=i.id)
            if fl[0]['results'] > 0:
                i.followup = True
            else:
                i.followup = False

            # patient name and phone number
            # i.patient_name = handle_result(
            #     users_service.get_one(db=db, id=i.patient_id)).name
            # i.patient_phone = handle_result(
            #     users_service.get_one(db=db, id=i.patient_id)).phone

            patient_name_phone = users_repo.get_one(db=db, id=i.patient_id)
            if patient_name_phone:
                i.patient_name = patient_name_phone.name
                i.patient_phone = patient_name_phone.phone

            new_data.append(i)

        final_data.append(new_data)

        if not final_data:
            [{"results": 0}, []]
        else:
            return ServiceResult(final_data, status_code=status.HTTP_201_CREATED)
    # order keyword
    # --------------
    # medicine order = medicine_order

    ###############################
    #                             #
    #    Medicine Service Order   #
    #                             #
    ###############################

    def medicine_order(self, db: Session, data_in: List[Union[ServiceOrderIn, List[MedicineOrderIn]]], user_id: int):

        # service
        data_obj = data_in[0].dict(exclude={'service_name'})
        data_obj.update({"service_name": "medicine_order"})
        service_flash = self.create_with_flush(
            db=db, data_in=ServiceOrderIn(**data_obj))
        # print(service_flash.id)

        # medicine
        medicine_list_len = len(data_in[1])
        i = 0
        while i < medicine_list_len:
            medicine_order_service.create_with_flush(db=db, data_in=MedicineOrderInWithService(
                service_order_id=handle_result(service_flash).id, **data_in[1][i].dict()))
            i += 1

        patient_user = users_service.get_one(db=db, id=data_in[0].patient_id)

        # activitylog
        created_by_employee_data = AdminPanelActivityIn(
            user_id=user_id,
            service_name="medicine_order",
            service_recived_id=handle_result(service_flash).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(
            db=db, data_in=created_by_employee_data)

        if not created_by_employee:
            return ServiceResult(AppException.ServerError("Problem with Medicine order."))
        else:
            s = sms_service.send_sms(
                sms_to='88'+handle_result(patient_user).phone,
                sms='আপনার মেডিসিনের অর্ডার টি সঠিক ভাবে নেয়া হয়েছে। শীঘ্রই আপনার অর্ডার টি ডেলিভারি করা হবে। অর্ডার সংক্রান্ত যেকোনো তথ্য জানতে সরাসরি যোগাযোগ করুন 01571-016461, 01322-658481 এই নাম্বারে। \nধন্যবাদান্তে \nHEALTHx')
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


service_order_service = ServiceOrderService(ServiceOrder, service_order_repo)
