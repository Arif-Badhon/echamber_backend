from repositories import BaseRepo, UpdateSchemaType, ModelType
from models import UserDetail
from schemas import UserDetailIn, UserDetailUpdate
from sqlalchemy.orm import Session


class UserDetailRepo(BaseRepo[UserDetail,
                              UserDetailIn, UserDetailUpdate]):

    def get_by_user_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.user_id == id).first()

    def update_by_user_id(self, db: Session, user_id: int,  data_update: UpdateSchemaType) -> ModelType:
        db.query(self.model).filter(self.model.user_id == user_id).update(
            data_update.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return self.get_by_user_id(db, id=user_id)


user_details_repo = UserDetailRepo(UserDetail)
