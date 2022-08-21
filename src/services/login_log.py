from services import BaseService
from repositories import login_log_repo, users_repo
from models import LoginLog
from schemas import LoginLogIn, LoginLogUpdate
from sqlalchemy.orm import Session
from exceptions import ServiceResult
from fastapi import status


class LoginLogService(BaseService[LoginLog, LoginLogIn, LoginLogUpdate]):
    def all_log_with_user(self, db: Session, skip: int, limit: int):
        data = self.repo.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)
        new_data = [{"results": data[0]["results"]}, []]

        for i in data[1]:
            u = users_repo.get_one(db=db, id=i.user_id)
            i.name = u.name
            new_data[1].append(i)

        if not new_data:
            new_data = []
        return ServiceResult(data, status_code=status.HTTP_200_OK)


login_log_services = LoginLogService(LoginLog, login_log_repo)
