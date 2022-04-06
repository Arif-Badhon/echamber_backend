from typing import Optional
from sqlalchemy.orm import Session
from repositories import BaseRepo, UpdateSchemaType, ModelType
from schemas import UserCreate, UserUpdate
from models import User, Role


class UserRepo(BaseRepo[User, UserCreate, UserUpdate]):
    def search_by_email(self, db: Session, email_in: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email_in).first()

    def search_by_phone(self, db: Session, phone_in: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.phone == phone_in).first()

    def update_by_user_id(self, db: Session, user_id: int,  data_update: UpdateSchemaType) -> ModelType:
        db.query(self.model).filter(self.model.id == user_id).update(
            data_update.dict(exclude_unset=True), synchronize_session=False)
        db.commit()
        return self.get_one(db, id=user_id)


users_repo = UserRepo(User)
