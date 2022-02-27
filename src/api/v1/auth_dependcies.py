from fastapi import Depends
from pydantic import ValidationError
from models import User
from db.core import settings
from db import get_db
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from exceptions.app_exceptions import AppException
from exceptions.service_result import ServiceResult, handle_result
from jose import jwt
from schemas import TokenPayload
from services import users_service

Oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=f"{settings.API_V1_STR}/login"
)


def get_current_user(
    db: Session = Depends(get_db), token: str = Depends(Oauth2_scheme)
) -> User:
    try:
        payload = jwt.decode(
            token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM]
        )
        token_data = TokenPayload(**payload)
    except (jwt.JWTError, ValidationError):
        return ServiceResult(AppException.CredentialsException())

    return users_service.search_by_email_service(db, email_in=token_data.sub)


def get_current_active_user(
    current_user: User = Depends(get_current_user),
) -> User:
    if not handle_result(current_user).is_active:
        return ServiceResult(AppException.Forbidden("Inactive user"))

    return current_user


# We need to specify role
