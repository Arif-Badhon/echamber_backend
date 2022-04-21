from __future__ import division
from exceptions.app_exceptions import AppException
from exceptions.service_result import ServiceResult
from services import BaseService, UpdateSchemaType
from repositories import user_details_repo
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate
from sqlalchemy.orm import Session
from fastapi import status


class UserDetailService(BaseService[UserDetail, UserDetailIn, UserDetailUpdate]):
    def get_by_user_id(self, db: Session, id: int):
        user_detail = self.repo.get_by_user_id(db, id)
        if not user_detail:
            return ServiceResult(AppException.NotFound("User detail not found"))
        else:
            return ServiceResult(user_detail, status_code=status.HTTP_200_OK)

    def update_by_user_id(self, db: Session, user_id: int, data_update: UpdateSchemaType):
        data = self.repo.update_by_user_id(db, user_id, data_update)
        if not data:
            return ServiceResult(AppException.NotAccepted())
        return ServiceResult(data, status_code=status.HTTP_202_ACCEPTED)


user_details_service = UserDetailService(UserDetail, user_details_repo)
