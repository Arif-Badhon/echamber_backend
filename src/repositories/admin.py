from sqlalchemy.orm import Session
from repositories import BaseRepo
from .roles import roles_repo
from schemas import UserCreate, UserUpdate
from models import User, Doctor


class AdminRepo(BaseRepo[User, UserCreate, UserUpdate]):

    def search_by_role_id(self, db: Session, id: int):
        return db.query(self.model).filter(self.model.role_id == id).all()

    def all_moderators(self, db: Session):
        moderator_id = roles_repo.search_name_id(db, name='moderator')
        query = db.query(self.model).filter(
            self.model.role_id == moderator_id).all()
        return query

    def doctors_inactive_list(self, db: Session):
        doctor_role_id = roles_repo.search_name_id(db, name='doctor')
        query = db.query(User, Doctor).join(Doctor).filter(
            User.role_id == doctor_role_id).filter(User.is_active == False).all()
        return query

    def doctor_active_by_id(self, db: Session, id):
        db.query(self.model).filter(self.model.id == id).update(
            {self.model.is_active: True}, synchronize_session=False)
        db.commit()
        return self.get_one(db, id)


admin_repo = AdminRepo(User)
