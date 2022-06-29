from sqlalchemy.orm import Session
from fastapi import status
from exceptions.service_result import handle_result
from services import BaseService
from models import FollowUp
from schemas import FollowUpIn, FollowUpInWithServiceId, FollowUpUpdate, AdminPanelActivityIn
from repositories import follow_up_repo, admin_panel_activity_repo
from exceptions import ServiceResult, AppException, handle_result


class FollowUpService(BaseService[FollowUp, FollowUpInWithServiceId, FollowUpUpdate]):

    def create_with_service(self, db: Session, data_in:FollowUpIn, service_id: int, user_id: int):
        fls = follow_up_service.create_with_flush(db=db, data_in=FollowUpInWithServiceId(**data_in.dict(), service_id=service_id))
        if not fls:
            return ServiceResult(AppException.ServerError("Something went wrong!"))
        
        activity = admin_panel_activity_repo.create(db=db, data_in=AdminPanelActivityIn(
                user_id= user_id,
                service_name="follow_up",
                service_recived_id=handle_result(fls).id,
                remark=""))


        if not activity:
            return ServiceResult(AppException.ServerError("Problem with follow-up."))
        else:
            return ServiceResult(activity, status_code=status.HTTP_201_CREATED)

follow_up_service = FollowUpService(FollowUp, follow_up_repo)