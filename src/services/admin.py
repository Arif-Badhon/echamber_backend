from exceptions.service_result import handle_result
from services import BaseService
from .users import users_service
from schemas import UserCreate, UserUpdate, AdminPanelActivityIn
from models import User
from repositories import admin_repo, roles_repo, admin_panel_activity_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class Admin(BaseService[User, UserCreate, UserUpdate]):

    def signup_admin(self, db: Session, data_in: UserCreate):

        admin_id = roles_repo.search_name_id(db, name='admin')

        admin_exist = self.repo.search_by_role_id(db, id=admin_id)

        if not admin_exist:
            sginup_data = UserCreate(
                name=data_in.name,
                email=data_in.email,
                phone=data_in.phone,
                sex=data_in.sex,
                is_active=True,
                password=data_in.password,
                role_name='admin'
            )

            signup_admin = users_service.signup(
                db, data_in=sginup_data, flush=False)

            return signup_admin

        return ServiceResult(AppException.ServerError('Admin exist'))

    def signup_employee(self, db: Session, data_in: UserCreate, creator_id: int):

        sginup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name=data_in.role_name
        )

        signup_employee = users_service.signup(
            db, data_in=sginup_data, flush=True)
        
        created_by_employee_data = AdminPanelActivityIn(
            user_id=creator_id,
            service_name="employee_register",
            service_recived_id=handle_result(signup_employee).id,
            remark=""
        )

        created_by_employee = admin_panel_activity_repo.create(db=db, data_in=created_by_employee_data)


        if not created_by_employee:
            return ServiceResult(AppException.ServerError(
                "Problem with patient registration."))
        else:
            return ServiceResult(created_by_employee, status_code=status.HTTP_201_CREATED)


    def all_employee(self, db: Session, skip: int=0, limit: int=10):
        all_emp = self.repo.all_employee(db, skip, limit)
        for i in all_emp:
            i.role_name = roles_repo.get_one(db=db, id=i.role_id).name 
        if not all_emp:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_emp, status_code=status.HTTP_200_OK)

    def doctor_active_list(self, db: Session):
        all_doc = self.repo.doctors_active_list(db)
        if not all_doc:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_doc, status_code=status.HTTP_200_OK)

    def doctor_inactive_list(self, db: Session):
        all_doc = self.repo.doctors_inactive_list(db)
        if not all_doc:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all_doc, status_code=status.HTTP_200_OK)

    def doctor_active_id(self, db: Session, id: int):
        active = self.repo.doctor_active_by_id(db, id)

        return self.get_one(db, id)


admin_service = Admin(User, admin_repo)
