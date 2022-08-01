from models import DfPost
from schemas import DfPostIn, DfPostUpdate
from services import BaseService
from repositories import df_post_repo, image_log_repo
from sqlalchemy.orm import Session
from exceptions import ServiceResult
from fastapi import status


class DfPostService(BaseService[DfPost, DfPostIn, DfPostUpdate]):

    def post_out(self, skip: int, limit: int, db: Session):
        data = df_post_repo.get_with_pagination(db=db, skip=skip, limit=limit, descending=True, count_results=True)

        for i in data[1]:
            d = image_log_repo.get_one(db=db, id=i.cover_image_id)
            if not d:
                i.cover_image_str = None
            else:
                i.cover_image_str = d.image_string

        return ServiceResult(data, status_code=status.HTTP_200_OK)


df_post_service = DfPostService(DfPost, df_post_repo)
