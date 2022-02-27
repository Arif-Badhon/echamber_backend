from typing import Optional
from sqlalchemy.orm import Session
from repositories import BaseRepo
from schemas import UserCreate, UserUpdate
from models import User, Role


class UserRepo(BaseRepo[User, UserCreate, UserUpdate]):
    def search_by_email(self, db: Session, email_in: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.email == email_in).first()

    def search_by_phone(self, db: Session, phone_in: str) -> Optional[User]:
        return db.query(self.model).filter(self.model.phone == phone_in).first()


users_repo = UserRepo(User)
