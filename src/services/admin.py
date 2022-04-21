from services import BaseService
from .users import users_service
from schemas import UserCreate, UserUpdate
from models import User
from repositories import admin_repo, roles_repo
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

    def signup_moderator(self, db: Session, data_in: UserCreate):

        sginup_data = UserCreate(
            name=data_in.name,
            email=data_in.email,
            phone=data_in.phone,
            sex=data_in.sex,
            is_active=True,
            password=data_in.password,
            role_name='moderator'
        )

        signup_moderator = users_service.signup(
            db, data_in=sginup_data, flush=False)

        return signup_moderator

    def all_moderator(self, db: Session):
        moderators = self.repo.all_moderators(db)
        if not moderators:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(moderators, status_code=status.HTTP_200_OK)

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
