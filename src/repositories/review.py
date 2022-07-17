from models import Review
from repositories import BaseRepo
from schemas import ReviewIn, ReviewUdate
from sqlalchemy.orm import Session


class ReviewRepo(BaseRepo[Review, ReviewIn, ReviewUdate]):

    def visibility(self, db: Session, id: int):
        current_visibility = self.get_one(db=db, id=id).visible
        data = self.update(db=db, id=id, data_update=ReviewUdate(visible=not current_visibility))
        return data


review_repo = ReviewRepo(Review)
