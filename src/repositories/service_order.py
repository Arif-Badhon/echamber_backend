from sqlalchemy import desc
from models import ServiceOrder, User
from schemas import ServiceOrderIn, ServiceOrderUpdate
from repositories import BaseRepo
from sqlalchemy.orm import Session
from sqlalchemy import or_, func


class ServiceOrderRepo(BaseRepo[ServiceOrder, ServiceOrderIn, ServiceOrderUpdate]):

    def service_with_patient(
            self, db: Session, service_id: int, customer_id: int, customer_name: str, customer_phone: str, address: str, service_name: str, start_date: str, end_date: str, order_date: str,
            order_status: str, skip: int, limit: int):

        if customer_name is None:
            customer_name = ''
        if customer_phone is None:
            customer_phone = ''
        if address is None:
            address = ''
        if service_name is None:
            service_name = ''
        if order_date is None:
            order_date = ''
        if order_status is None:
            order_status = ''
        # if start_date is None:
        #     start_date = ''
        # if end_date is None:
        #     end_date = ''

        if service_id is not None:
            data = db.query(ServiceOrder, User).join(User, User.id == ServiceOrder.patient_id).filter(ServiceOrder.id == service_id).offset(skip).limit(limit).all()
            return [{"results": len(data)}, data]
        elif customer_id is not None:
            data = db.query(ServiceOrder, User).join(User, User.id == ServiceOrder.patient_id).filter(User.id == customer_id).offset(skip).limit(limit).all()
            return [{"results": len(data)}, data]
        elif start_date is not None:
            data_all = db.query(
                ServiceOrder, User).join(
                User, User.id == ServiceOrder.patient_id).filter(
                ServiceOrder.service_name.like(f"%{service_name}%")).filter(
                ServiceOrder.order_placement.between(start_date, end_date)).filter(
                ServiceOrder.current_address.like(f"%{address}%")).filter(or_(
                    ServiceOrder.order_status.like(f"%{order_status}%"),
                    ServiceOrder.order_status == None)).filter(
                User.name.like(f"%{customer_name}%")).filter(
                User.phone.like(f"%{customer_phone}%")).all()
            data = db.query(
                ServiceOrder, User).join(
                User, User.id == ServiceOrder.patient_id).filter(
                ServiceOrder.service_name.like(f"%{service_name}%")).filter(
                ServiceOrder.order_placement.between(start_date, end_date)).filter(
                ServiceOrder.current_address.like(f"%{address}%")).filter(or_(
                    ServiceOrder.order_status.like(f"%{order_status}%"),
                    ServiceOrder.order_status == None)).filter(
                User.name.like(f"%{customer_name}%")).filter(
                User.phone.like(f"%{customer_phone}%")).order_by(desc(self.model.order_placement)).offset(skip).limit(limit).all()

            return [{"results": len(data_all)}, data]
        else:
            data_all = db.query(
                ServiceOrder, User).join(
                User, User.id == ServiceOrder.patient_id).filter(
                ServiceOrder.service_name.like(f"%{service_name}%")).filter(
                ServiceOrder.order_placement.like(f"%{order_date}%")).filter(
                ServiceOrder.current_address.like(f"%{address}%")).filter(or_(
                    ServiceOrder.order_status.like(f"%{order_status}%"),
                    ServiceOrder.order_status == None)).filter(
                User.name.like(f"%{customer_name}%")).filter(
                User.phone.like(f"%{customer_phone}%")).all()
            data = db.query(
                ServiceOrder, User).join(
                User, User.id == ServiceOrder.patient_id).filter(
                ServiceOrder.service_name.like(f"%{service_name}%")).filter(
                ServiceOrder.order_placement.like(f"%{order_date}%")).filter(
                ServiceOrder.current_address.like(f"%{address}%")).filter(or_(
                    ServiceOrder.order_status.like(f"%{order_status}%"),
                    ServiceOrder.order_status == None)).filter(
                User.name.like(f"%{customer_name}%")).filter(
                User.phone.like(f"%{customer_phone}%")).order_by(desc(self.model.order_placement)).offset(skip).limit(limit).all()

            return [{"results": len(data_all)}, data]

    def patient_with_multiservice(self, db: Session):
        data = db.query(ServiceOrder.patient_id, func.count(ServiceOrder.patient_id)).group_by(ServiceOrder.patient_id).having(func.count(ServiceOrder.patient_id) > 1).all()
        data_len = len(data)
        return data_len

    def patient_with_multiservice_range(self, db: Session, start_date: str, end_date: str):
        data = db.query(ServiceOrder.patient_id, func.count(ServiceOrder.patient_id)).filter(
            ServiceOrder.order_placement.between(start_date, end_date)).group_by(ServiceOrder.patient_id).having(func.count(ServiceOrder.patient_id) > 1).all()
        data_len = len(data)
        return data_len


service_order_repo = ServiceOrderRepo(ServiceOrder)
