from datetime import timedelta
from sqlalchemy.orm import Session
from db.db_session import get_db
from exceptions import ServiceResult
from exceptions import AppException, handle_result
from repositories import users_repo, roles_repo
from services import BaseService
from models import User
from schemas import UserCreate, UserUpdate, UserDBIn
from utils import password_hash, create_access_token, verify_password
from fastapi import Depends, status
from db import settings
from fastapi.security import OAuth2PasswordRequestForm


class UserService(BaseService[User, UserCreate, UserUpdate]):

    def signup(self, db: Session, data_in: UserCreate):

        # Email and phone check
        if self.repo.search_by_email(db, data_in.email):
            return ServiceResult(AppException.BadRequest("Email already exist."))
        if self.repo.search_by_phone(db, data_in.phone):
            return ServiceResult(AppException.BadRequest("Phone number already exist."))

        # role id from role name
        role = roles_repo.search_name_id(db, data_in.role_name)

        data_obj = data_in.dict(exclude={"password", "role_name"})
        password = password_hash(data_in.password)
        data_obj.update({"password": password})

        data = self.repo.create(db, data_in=UserDBIn(
            **data_obj, role_id=role))

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    # Need this for Deps

    def search_by_email_service(self, db: Session, email_in: str):
        data = self.repo.search_by_email(db, email_in)
        if not data:
            return ServiceResult(
                AppException.NotFound(
                    f"No user found with this email: {email_in}")
            )
        return ServiceResult(data, status_code=status.HTTP_200_OK)

    def is_auth(self, db: Session, identifier: str, password: str):
        user_by_email = self.repo.search_by_email(db, email_in=identifier)
        user_by_phone = self.repo.search_by_phone(db, phone_in=identifier)

        if user_by_email and verify_password(password, user_by_email.password):
            return user_by_email
        elif user_by_phone and verify_password(password, user_by_phone.password):
            return user_by_phone
        else:
            return None

    # def login(self, db: Session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    #     user = self.is_auth(db, identifier=form_data.username,
    #                         password=form_data.password)

    #     if not user:
    #         return handle_result(
    #             ServiceResult(AppException.BadRequest(
    #                 "Incorrect username or password"))
    #         )
    #     elif not user.is_active:
    #         return handle_result(ServiceResult(AppException.BadRequest("User is inactive")))

    #     access_token_expires = timedelta(
    #         minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)

    #     access_token = create_access_token(user.email, access_token_expires)

    #     return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)


users_service = UserService(User, users_repo)
