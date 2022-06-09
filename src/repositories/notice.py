from sqlalchemy import desc
from repositories import BaseRepo
from schemas import NoticeIn, NoticeUpdate, NoticeBase
from models import Notice
from sqlalchemy.orm import Session

from schemas.notice import NoticeBase


class NoticeRepo(BaseRepo[Notice, NoticeIn, NoticeUpdate]):

    def all_notice(self, db:Session, skip: int, limit: int):
        query = db.query(self.model).order_by(desc(self.model.created_at)).offset(skip).limit(limit).all()
        return query

    def create_with_user(self, db: Session, data_in:NoticeBase, user_id: int):
        data_for_db = NoticeIn(user_id=user_id, **data_in.dict())
        notice = self.create(db=db, data_in=data_for_db)
        return notice

    def active_switch(self, db: Session, id:int):
        current_status = self.get_one(db=db, id=id).status
        up = self.update(db=db, id=id, data_update=NoticeUpdate(status = not current_status))
        return up 


notice_repo = NoticeRepo(Notice)