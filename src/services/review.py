from exceptions.service_result import handle_result
from models import Review
from schemas import ReviewIn, ReviewUdate
from services import BaseService
from repositories import review_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult, AppException
from fastapi import status


class ReviewService(BaseService[Review, ReviewIn, ReviewUdate]):

    def visibility(self, db: Session, id: int):
        data = self.repo.visibility(db=db, id=id)

        if not data:
            return ServiceResult(AppException.ServerError("Review visibility not changed"))
        else:
            return ServiceResult(data, status_code=status.HTTP_201_CREATED)

    def delete_review(self, db: Session, id: int, user_id: int):
        review_user_id = self.get_one(db=db, id=id)
        if handle_result(review_user_id).user_id != user_id:
            return ServiceResult(AppException.ServerError("Not valid author"))

        data = self.delete(db=db, id=id)
        return data


review_service = ReviewService(Review, review_repo)
