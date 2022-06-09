from exceptions.service_result import handle_result
from services import BaseService
from repositories import notice_repo
from models import Notice
from schemas import NoticeIn, NoticeUpdate, NoticeBase
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException, handle_result
from fastapi import status

class NoticeService(BaseService[Notice, NoticeIn, NoticeUpdate]):

    def all_notice(self, db:Session, skip: int, limit: int):
        all = self.repo.all_notice(db=db, skip=skip, limit=limit)
        
        if not all:
            return ServiceResult([], status_code=status.HTTP_200_OK)
        else:
            return ServiceResult(all, status_code=status.HTTP_200_OK)



    def create_with_user(self, db: Session, data_in: NoticeBase, user_id: int):
        notice = self.repo.create_with_user(db=db, data_in=data_in,user_id=user_id)

        if not notice:
            return ServiceResult(AppException.ServerError("Notice not posted"))
        else:
            return ServiceResult(notice, status_code=status.HTTP_201_CREATED)



    def active_switch(self, db: Session, id: int):
        actv = self.repo.active_switch(db=db, id=id)
        
        if not actv:
            return ServiceResult(AppException.ServerError("Notice not posted"))
        else:
            return ServiceResult(actv, status_code=status.HTTP_201_CREATED)

notice_service = NoticeService(Notice, notice_repo)