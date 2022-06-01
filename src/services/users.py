from exceptions.service_result import handle_result
from schemas.users import NewPasswordIn
from utils import Token
from sqlalchemy.orm import Session
from exceptions import ServiceResult
from exceptions import AppException
from repositories import users_repo, roles_repo, UpdateSchemaType
from services import BaseService
from .roles import roles_service
from models import User
from schemas import UserCreate, UserUpdate, UserDBIn
from utils import password_hash, verify_password
from fastapi import status


class UserService(BaseService[User, UserCreate, UserUpdate]):

    def signup(self, db: Session, data_in: UserCreate, flush: bool):

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

        # data: User = None
        if not flush:
            data = self.repo.create(db, data_in=UserDBIn(
                **data_obj, role_id=role))
        else:
            data = self.repo.create_with_flush(db, data_in=UserDBIn(
                **data_obj, role_id=role))

        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    
    def user_update(self, db: Session, id:int,  data_update:UserUpdate):

        data = self.repo.update(db, id, data_update)
        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)


    def user_id(self, db: Session, id: int):
        data = self.get_one(db=id,id=id)
        role_name = roles_service.get_one(db=db, id=handle_result(data).role_id).name
        data.role_name = role_name
        if not data:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        return ServiceResult(data, status_code=status.HTTP_201_CREATED)


    def user_search_by_phone(self, db: Session, phone_in: str='0', skip: int=0, limit:int = 10):
        data_all = users_repo.search_by_phone_all(db=db, phone_in=phone_in, skip=skip, limit=limit)
        data = []

        for i in data_all:
            role_name = roles_service.get_one(db=db, id=i.role_id)
            i.role_name = handle_result(role_name).name
            data.append(i)
        if not data:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        return ServiceResult(data, status_code=status.HTTP_200_OK)



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

    def login(self, db: Session, identifier: str, password: str):
        user: User = self.is_auth(db, identifier, password)
        if user is not None:
            access_token = Token.create_access_token({"sub": user.id})
            return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)
        else:
            return ServiceResult(AppException.NotFound("User not found"))

    def new_password(self, db: Session, user_id: int, data_update: UpdateSchemaType):

        data_obj = data_update.dict(exclude={"password"})
        password = password_hash(data_update.password)
        data_obj.update({"password": password})

        data = self.repo.update_by_user_id(
            db, user_id, data_update=NewPasswordIn(**data_obj))
        if not data:
            return ServiceResult(AppException.NotAccepted())
        access_token = Token.create_access_token({"sub": user_id})
        return ServiceResult({"access_token": access_token, "token_type": "bearer"}, status_code=200)


users_service = UserService(User, users_repo)
