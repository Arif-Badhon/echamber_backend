from sqlalchemy.orm import Session
from repositories import BaseRepo
from schemas import UserCreate, UserUpdate
from models import User


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()


admin_repo = AdminRepo(User)
