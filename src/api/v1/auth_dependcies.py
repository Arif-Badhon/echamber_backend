from fastapi import Depends
from db import get_db
from fastapi.security import HTTPBasicCredentials, HTTPBearer
from sqlalchemy.orm import Session
from exceptions.app_exceptions import AppException
from exceptions.service_result import handle_result
from services import users_service, roles_service
from utils import Token

security = HTTPBearer()

# "name": "admin"
# "name": "moderator"
# "name": "doctor"
# "name": "patient"
# "name": "sales"
# "name": "medical_affairs"


def logged_in(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    token = credentials.credentials
    token_data = Token.validate_token(token)
    user = handle_result(users_service.get_one(db, id=token_data.user_id))
    role_name = roles_service.get_one(db, id=user.role_id)
    user.role_name = handle_result(role_name).name

    if not user:
        raise AppException.Unauthorized()
    return user


def logged_in_admin(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name != 'admin'):
        raise AppException.Unauthorized()

    if not user:
        raise AppException.Unauthorized()
    return user


def logged_in_moderator(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name != 'moderator'):
        raise AppException.Unauthorized()

    if not user:
        raise AppException.Unauthorized()
    return user


def logged_in_admin_moderator(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name == 'admin' or role_name_obj.name == 'moderator'):
        if not user:
            raise AppException.Unauthorized()
        return user
    else:
        raise AppException.Unauthorized()


def logged_in_admin_medical_affairs(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name == 'admin' or role_name_obj.name == 'medical_affairs'):
        if not user:
            raise AppException.Unauthorized()
        return user
    else:
        raise AppException.Unauthorized()


def logged_in_admin_crm(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name == 'admin' or role_name_obj.name == 'crm'):
        if not user:
            raise AppException.Unauthorized()
        return user
    else:
        raise AppException.Unauthorized()


def logged_in_employee(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name == 'doctor' or role_name_obj.name == 'patient'):
        raise AppException.Unauthorized()
    else:
        if not user:
            raise AppException.Unauthorized()
        return user


def logged_in_doctor(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name != 'doctor'):
        raise AppException.Unauthorized()

    if not user:
        raise AppException.Unauthorized()
    return user


def logged_in_patient(credentials: HTTPBasicCredentials = Depends(security), db: Session = Depends(get_db)):
    user = logged_in(credentials, db)

    role_name = roles_service.get_one(db, user.role_id)
    role_name_obj = handle_result(role_name)

    if(role_name_obj.name != 'patient'):
        raise AppException.Unauthorized()

    if not user:
        raise AppException.Unauthorized()
    return user
